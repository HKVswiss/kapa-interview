import logging
import re
from typing import Dict, List, Tuple, Optional
from dataclasses import dataclass

import pymupdf
import pytesseract
from PIL import Image
import numpy as np

from src.loader.types import LoadedPDF
from src.converter.base import PDFtoMarkdown

logger = logging.getLogger(__name__)


@dataclass
class TextBlock:
    """Represents a block of text with its properties."""
    text: str
    bbox: Tuple[float, float, float, float]  # x0, y0, x1, y1
    font_size: float
    font_name: str
    is_bold: bool
    is_italic: bool
    page_num: int


class HybridOCRConverter(PDFtoMarkdown):
    """
    Hybrid PDF to Markdown converter combining:
    1. PyMuPDF text extraction for native text
    2. OCR for scanned/image content
    3. Layout analysis for structure detection
    4. Table detection and extraction
    """
    
    def __init__(
        self, 
        ocr_fallback: bool = True,
        table_detection: bool = True,
        dpi: int = 300,
        tesseract_config: str = "--oem 3 --psm 6"
    ):
        self.ocr_fallback = ocr_fallback
        self.table_detection = table_detection
        self.dpi = dpi
        self.tesseract_config = tesseract_config
        
        # Check if tesseract is available
        try:
            pytesseract.get_tesseract_version()
            self.ocr_available = True
        except Exception:
            logger.warning("Tesseract not available, OCR disabled")
            self.ocr_available = False
    
    def convert(self, doc: LoadedPDF) -> str:
        """Convert PDF using hybrid approach."""
        try:
            pdf_document = pymupdf.open(stream=doc.raw_bytes, filetype="pdf")
            
            # Extract content from all pages
            all_blocks = []
            for page_num in range(len(pdf_document)):
                page_blocks = self._extract_page_content(pdf_document, page_num)
                all_blocks.extend(page_blocks)
            
            # Structure the content into markdown
            markdown = self._structure_to_markdown(all_blocks, doc.name)
            
            pdf_document.close()
            return markdown
            
        except Exception as e:
            logger.error(f"Error in hybrid conversion of {doc.name}: {e}")
            return self._fallback_convert(doc)
    
    def _extract_page_content(self, pdf_doc: pymupdf.Document, page_num: int) -> List[TextBlock]:
        """Extract content from a single page using multiple methods."""
        page = pdf_doc[page_num]
        blocks = []
        
        # Method 1: Extract native text with formatting
        native_blocks = self._extract_native_text(page, page_num)
        blocks.extend(native_blocks)
        
        # Method 2: OCR for areas with little/no native text
        if self.ocr_available and self._needs_ocr(page, native_blocks):
            ocr_blocks = self._extract_ocr_text(page, page_num)
            blocks.extend(ocr_blocks)
        
        # Method 3: Table detection
        if self.table_detection:
            table_blocks = self._extract_tables(page, page_num)
            blocks.extend(table_blocks)
        
        return blocks
    
    def _extract_native_text(self, page: pymupdf.Page, page_num: int) -> List[TextBlock]:
        """Extract native text with formatting information."""
        blocks = []
        
        # Get text with detailed formatting
        text_dict = page.get_text("dict")
        
        for block in text_dict.get("blocks", []):
            if "lines" not in block:  # Skip image blocks
                continue
                
            for line in block["lines"]:
                for span in line["spans"]:
                    text = span["text"].strip()
                    if not text:
                        continue
                    
                    # Extract formatting
                    font_info = span.get("font", "")
                    font_size = span.get("size", 12)
                    flags = span.get("flags", 0)
                    
                    is_bold = bool(flags & 2**4)  # Bold flag
                    is_italic = bool(flags & 2**1)  # Italic flag
                    
                    # Create text block
                    bbox = span["bbox"]
                    text_block = TextBlock(
                        text=text,
                        bbox=bbox,
                        font_size=font_size,
                        font_name=font_info,
                        is_bold=is_bold,
                        is_italic=is_italic,
                        page_num=page_num
                    )
                    blocks.append(text_block)
        
        return blocks
    
    def _needs_ocr(self, page: pymupdf.Page, native_blocks: List[TextBlock]) -> bool:
        """Determine if page needs OCR based on native text coverage."""
        # Simple heuristic: if very little native text, try OCR
        total_native_text = sum(len(block.text) for block in native_blocks)
        return total_native_text < 100  # Threshold for "sparse" text
    
    def _extract_ocr_text(self, page: pymupdf.Page, page_num: int) -> List[TextBlock]:
        """Extract text using OCR."""
        if not self.ocr_available:
            return []
        
        try:
            # Render page as image
            mat = pymupdf.Matrix(self.dpi / 72, self.dpi / 72)
            pix = page.get_pixmap(matrix=mat)
            img_data = pix.tobytes("png")
            pix = None
            
            # Convert to PIL Image
            image = Image.open(BytesIO(img_data))
            
            # Perform OCR with bounding boxes
            ocr_data = pytesseract.image_to_data(
                image, 
                config=self.tesseract_config,
                output_type=pytesseract.Output.DICT
            )
            
            blocks = []
            for i in range(len(ocr_data['text'])):
                text = ocr_data['text'][i].strip()
                if not text or int(ocr_data['conf'][i]) < 50:  # Low confidence
                    continue
                
                # Convert pixel coordinates back to PDF coordinates
                scale = 72 / self.dpi
                x = ocr_data['left'][i] * scale
                y = ocr_data['top'][i] * scale
                w = ocr_data['width'][i] * scale
                h = ocr_data['height'][i] * scale
                
                bbox = (x, y, x + w, y + h)
                
                text_block = TextBlock(
                    text=text,
                    bbox=bbox,
                    font_size=12,  # Default size for OCR
                    font_name="ocr",
                    is_bold=False,
                    is_italic=False,
                    page_num=page_num
                )
                blocks.append(text_block)
            
            return blocks
            
        except Exception as e:
            logger.warning(f"OCR failed for page {page_num}: {e}")
            return []
    
    def _extract_tables(self, page: pymupdf.Page, page_num: int) -> List[TextBlock]:
        """Detect and extract tables."""
        # Simple table detection using pymupdf
        try:
            tables = page.find_tables()
            table_blocks = []
            
            for table in tables:
                # Extract table as markdown
                table_data = table.extract()
                if not table_data:
                    continue
                
                # Convert to markdown table
                markdown_table = self._format_table_as_markdown(table_data)
                
                # Create a text block for the table
                bbox = table.bbox
                table_block = TextBlock(
                    text=markdown_table,
                    bbox=bbox,
                    font_size=12,
                    font_name="table",
                    is_bold=False,
                    is_italic=False,
                    page_num=page_num
                )
                table_blocks.append(table_block)
            
            return table_blocks
            
        except Exception as e:
            logger.warning(f"Table extraction failed for page {page_num}: {e}")
            return []
    
    def _format_table_as_markdown(self, table_data: List[List[str]]) -> str:
        """Format extracted table data as markdown table."""
        if not table_data:
            return ""
        
        # Clean and format rows
        rows = []
        for row in table_data:
            cleaned_row = [str(cell).strip() if cell else "" for cell in row]
            rows.append(cleaned_row)
        
        if not rows:
            return ""
        
        # Create markdown table
        markdown_lines = []
        
        # Header row
        header = "| " + " | ".join(rows[0]) + " |"
        separator = "| " + " | ".join(["---"] * len(rows[0])) + " |"
        
        markdown_lines.append(header)
        markdown_lines.append(separator)
        
        # Data rows
        for row in rows[1:]:
            if len(row) == len(rows[0]):  # Ensure consistent columns
                row_md = "| " + " | ".join(row) + " |"
                markdown_lines.append(row_md)
        
        return "\n".join(markdown_lines)
    
    def _structure_to_markdown(self, blocks: List[TextBlock], filename: str) -> str:
        """Convert text blocks to structured markdown."""
        if not blocks:
            return f"# {filename}\n\nNo content extracted."
        
        # Sort blocks by page and position
        blocks.sort(key=lambda b: (b.page_num, b.bbox[1], b.bbox[0]))
        
        # Group by page
        pages = {}
        for block in blocks:
            if block.page_num not in pages:
                pages[block.page_num] = []
            pages[block.page_num].append(block)
        
        # Convert to markdown
        markdown_parts = [f"# {filename.replace('.pdf', '').replace('_', ' ').title()}"]
        
        for page_num in sorted(pages.keys()):
            page_blocks = pages[page_num]
            page_md = self._process_page_blocks(page_blocks, page_num)
            if page_md.strip():
                markdown_parts.append(f"\n<!-- Page {page_num + 1} -->\n")
                markdown_parts.append(page_md)
        
        return "\n\n".join(markdown_parts)
    
    def _process_page_blocks(self, blocks: List[TextBlock], page_num: int) -> str:
        """Process blocks from a single page into markdown."""
        if not blocks:
            return ""
        
        lines = []
        
        for block in blocks:
            text = block.text.strip()
            if not text:
                continue
            
            # Format based on properties
            if block.font_name == "table":
                lines.append(text)  # Already formatted as markdown table
            elif self._is_heading(block):
                level = self._get_heading_level(block)
                lines.append(f"{'#' * level} {text}")
            elif block.is_bold:
                lines.append(f"**{text}**")
            elif block.is_italic:
                lines.append(f"*{text}*")
            else:
                lines.append(text)
        
        return "\n\n".join(lines)
    
    def _is_heading(self, block: TextBlock) -> bool:
        """Determine if a text block represents a heading."""
        # Simple heuristics for heading detection
        return (
            block.font_size > 14 or  # Large font
            block.is_bold or  # Bold text
            len(block.text) < 100  # Short text (potential title)
        )
    
    def _get_heading_level(self, block: TextBlock) -> int:
        """Determine heading level based on font size and other properties."""
        if block.font_size > 20:
            return 1
        elif block.font_size > 16:
            return 2
        elif block.font_size > 14:
            return 3
        else:
            return 4
    
    def _fallback_convert(self, doc: LoadedPDF) -> str:
        """Fallback to basic conversion."""
        try:
            import pymupdf4llm
            pdf = pymupdf.open(stream=doc.raw_bytes, filetype="pdf")
            markdown = pymupdf4llm.to_markdown(pdf, page_chunks=False)
            pdf.close()
            return f"# {doc.name}\n\n{markdown}"
        except Exception as e:
            logger.error(f"Fallback conversion failed for {doc.name}: {e}")
            return f"# {doc.name}\n\nConversion failed." 
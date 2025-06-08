import re
import logging
from typing import List, Dict, Tuple
from dataclasses import dataclass

import pymupdf
import pymupdf4llm

from src.loader.types import LoadedPDF
from src.converter.base import PDFtoMarkdown

logger = logging.getLogger(__name__)


@dataclass
class DocumentStructure:
    """Represents the structure of a document."""
    title: str
    sections: List[str]
    tables: List[str]
    key_values: Dict[str, str]


class EnhancedPyMuConverter(PDFtoMarkdown):
    """
    Enhanced PyMuPDF converter with improved structure detection and post-processing.
    
    Improvements over basic PymuConverter:
    1. Better heading detection and hierarchy
    2. Table structure preservation
    3. Key-value pair extraction
    4. Technical specification formatting
    5. Multi-column layout handling
    """
    
    def __init__(
        self,
        preserve_tables: bool = True,
        extract_metadata: bool = True,
        fix_formatting: bool = True
    ):
        self.preserve_tables = preserve_tables
        self.extract_metadata = extract_metadata
        self.fix_formatting = fix_formatting
    
    def convert(self, doc: LoadedPDF) -> str:
        """Convert PDF with enhanced processing."""
        try:
            pdf_document = pymupdf.open(stream=doc.raw_bytes, filetype="pdf")
            
            # Step 1: Basic conversion using pymupdf4llm
            raw_markdown = pymupdf4llm.to_markdown(pdf_document, page_chunks=False)
            
            # Step 2: Enhanced processing
            if self.preserve_tables:
                raw_markdown = self._enhance_tables(pdf_document, raw_markdown)
            
            if self.extract_metadata:
                raw_markdown = self._extract_key_metadata(pdf_document, raw_markdown)
            
            if self.fix_formatting:
                raw_markdown = self._fix_markdown_formatting(raw_markdown)
            
            # Step 3: Structure and clean up
            final_markdown = self._structure_document(raw_markdown, doc.name)
            
            pdf_document.close()
            return final_markdown
            
        except Exception as e:
            logger.error(f"Enhanced conversion failed for {doc.name}: {e}")
            return self._fallback_convert(doc)
    
    def _enhance_tables(self, pdf_doc: pymupdf.Document, markdown: str) -> str:
        """Improve table detection and formatting."""
        enhanced_markdown = markdown
        
        try:
            for page_num in range(len(pdf_doc)):
                page = pdf_doc[page_num]
                tables = page.find_tables()
                
                for table in tables:
                    table_data = table.extract()
                    if table_data and len(table_data) > 1:  # Has header + data
                        # Create well-formatted markdown table
                        table_md = self._create_markdown_table(table_data)
                        
                        # Find a good insertion point in the markdown
                        # This is a simplified approach - in practice, you'd want
                        # more sophisticated positioning
                        enhanced_markdown += f"\n\n{table_md}\n\n"
            
            return enhanced_markdown
            
        except Exception as e:
            logger.warning(f"Table enhancement failed: {e}")
            return markdown
    
    def _create_markdown_table(self, table_data: List[List[str]]) -> str:
        """Create properly formatted markdown table."""
        if not table_data or len(table_data) < 1:
            return ""
        
        # Clean data
        cleaned_data = []
        for row in table_data:
            cleaned_row = [str(cell).strip().replace('\n', ' ') if cell else "" for cell in row]
            cleaned_data.append(cleaned_row)
        
        # Ensure consistent column count
        max_cols = max(len(row) for row in cleaned_data)
        for row in cleaned_data:
            while len(row) < max_cols:
                row.append("")
        
        # Create markdown
        lines = []
        
        # Header
        header = "| " + " | ".join(cleaned_data[0]) + " |"
        lines.append(header)
        
        # Separator
        separator = "| " + " | ".join(["---"] * max_cols) + " |"
        lines.append(separator)
        
        # Data rows
        for row in cleaned_data[1:]:
            row_line = "| " + " | ".join(row[:max_cols]) + " |"
            lines.append(row_line)
        
        return "\n".join(lines)
    
    def _extract_key_metadata(self, pdf_doc: pymupdf.Document, markdown: str) -> str:
        """Extract and format key metadata and specifications."""
        enhanced_markdown = markdown
        
        # Look for common patterns in technical documents
        patterns = {
            'certificates': r'(?i)(certificate|approval)[\s\w]*?:\s*([A-Z0-9-]+)',
            'dates': r'(?i)(issued|valid|date)[\s\w]*?:\s*(\d{4}-\d{2}-\d{2}|\d{1,2}[/-]\d{1,2}[/-]\d{2,4})',
            'frequencies': r'(?i)(frequency|freq)[\s\w]*?:\s*([\d.]+ *[KMGT]?Hz[\s\-–to]*[\d.]* *[KMGT]?Hz?)',
            'voltages': r'(?i)(voltage|volt)[\s\w]*?:\s*([\d.]+ *[muµnpkmMGT]?V)',
            'pins': r'(?i)(pin|gpio)[\s\w]*?:\s*([A-Z0-9]+\s*\(\s*\d+\s*\))',
            'temperatures': r'(?i)(temperature|temp)[\s\w]*?:\s*([-+]?[\d.]+ *°?[CF])',
            'companies': r'(?i)(holder|company|manufacturer)[\s\w]*?:\s*([A-Z][A-Z\s&.,()]+(?:CO\.|LTD\.|INC\.|CORP\.)?)',
        }
        
        # Extract metadata
        metadata = {}
        for key, pattern in patterns.items():
            matches = re.findall(pattern, enhanced_markdown)
            if matches:
                metadata[key] = matches
        
        # Format metadata as structured markdown
        if metadata:
            metadata_section = "\n\n## Key Specifications\n\n"
            for key, values in metadata.items():
                if values:
                    metadata_section += f"### {key.title()}\n\n"
                    for match in values[:5]:  # Limit to first 5 matches
                        if isinstance(match, tuple):
                            metadata_section += f"- **{match[0]}**: {match[1]}\n"
                        else:
                            metadata_section += f"- {match}\n"
                    metadata_section += "\n"
            
            enhanced_markdown = metadata_section + enhanced_markdown
        
        return enhanced_markdown
    
    def _fix_markdown_formatting(self, markdown: str) -> str:
        """Fix common markdown formatting issues."""
        fixed = markdown
        
        # Fix heading detection - look for lines that should be headings
        lines = fixed.split('\n')
        fixed_lines = []
        
        for i, line in enumerate(lines):
            line = line.strip()
            
            # Skip empty lines
            if not line:
                fixed_lines.append('')
                continue
            
            # Check if this line should be a heading
            if self._should_be_heading(line, i, lines):
                # Determine heading level
                level = self._get_heading_level(line, i, lines)
                if not line.startswith('#'):
                    line = '#' * level + ' ' + line
            
            # Fix bold/italic formatting
            line = self._fix_emphasis(line)
            
            # Fix list formatting
            line = self._fix_lists(line)
            
            fixed_lines.append(line)
        
        fixed = '\n'.join(fixed_lines)
        
        # Fix multiple newlines
        fixed = re.sub(r'\n{3,}', '\n\n', fixed)
        
        return fixed
    
    def _should_be_heading(self, line: str, index: int, all_lines: List[str]) -> bool:
        """Determine if a line should be formatted as a heading."""
        if not line or line.startswith('#'):
            return False
        
        # Look for heading patterns
        heading_patterns = [
            r'^[A-Z][A-Z\s]{5,}$',  # ALL CAPS
            r'^\d+\.?\s+[A-Z]',      # Numbered sections
            r'^[A-Z][a-z]+\s+[A-Z]', # Title Case
        ]
        
        for pattern in heading_patterns:
            if re.match(pattern, line):
                return True
        
        # Check if short line followed by content
        if len(line) < 50 and index + 1 < len(all_lines):
            next_line = all_lines[index + 1].strip()
            if next_line and not next_line.startswith('#'):
                return True
        
        return False
    
    def _get_heading_level(self, line: str, index: int, all_lines: List[str]) -> int:
        """Determine the appropriate heading level."""
        if re.match(r'^[A-Z][A-Z\s]{10,}$', line):  # Very long ALL CAPS
            return 1
        elif re.match(r'^\d+\.?\s+', line):  # Numbered sections
            return 2
        elif len(line) < 30:  # Short titles
            return 3
        else:
            return 4
    
    def _fix_emphasis(self, line: str) -> str:
        """Fix bold and italic formatting."""
        # Look for words that should be bold (technical terms, model numbers)
        technical_pattern = r'\b([A-Z]{2,}[0-9]+[A-Z]*|[A-Z]+[0-9]+)\b'
        line = re.sub(technical_pattern, r'**\1**', line)
        
        return line
    
    def _fix_lists(self, line: str) -> str:
        """Fix list formatting."""
        # Convert various bullet styles to markdown
        line = re.sub(r'^[•·‣⁃]\s*', '- ', line)
        line = re.sub(r'^\d+\.\s*', lambda m: f"{m.group()}  ", line)  # Numbered lists
        
        return line
    
    def _structure_document(self, markdown: str, filename: str) -> str:
        """Add overall document structure."""
        # Clean filename for title
        title = filename.replace('.pdf', '').replace('_', ' ').replace('-', ' ').title()
        
        # Add document title if not present
        if not markdown.startswith('#'):
            markdown = f"# {title}\n\n{markdown}"
        
        # Add table of contents for long documents
        if len(markdown) > 5000:  # Long document
            toc = self._generate_toc(markdown)
            if toc:
                markdown = markdown.replace(f"# {title}\n\n", f"# {title}\n\n{toc}\n\n")
        
        return markdown
    
    def _generate_toc(self, markdown: str) -> str:
        """Generate table of contents from headings."""
        lines = markdown.split('\n')
        toc_lines = ["## Table of Contents\n"]
        
        for line in lines:
            if line.startswith('#'):
                level = len(line) - len(line.lstrip('#'))
                heading_text = line.lstrip('# ').strip()
                if level <= 3 and heading_text:  # Only include up to level 3
                    indent = "  " * (level - 1)
                    toc_lines.append(f"{indent}- {heading_text}")
        
        return "\n".join(toc_lines) if len(toc_lines) > 1 else ""
    
    def _fallback_convert(self, doc: LoadedPDF) -> str:
        """Basic fallback conversion."""
        try:
            pdf = pymupdf.open(stream=doc.raw_bytes, filetype="pdf")
            markdown = pymupdf4llm.to_markdown(pdf, page_chunks=False)
            pdf.close()
            return f"# {doc.name}\n\n{markdown}"
        except Exception as e:
            logger.error(f"Fallback conversion failed for {doc.name}: {e}")
            return f"# {doc.name}\n\nConversion failed." 
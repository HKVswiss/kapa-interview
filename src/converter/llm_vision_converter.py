import base64
import logging
from io import BytesIO
from typing import List, Optional

import pymupdf
from openai import OpenAI

from src.loader.types import LoadedPDF
from src.converter.base import PDFtoMarkdown

logger = logging.getLogger(__name__)


class LLMVisionConverter(PDFtoMarkdown):
    """
    Advanced PDF to Markdown converter using vision-language models.

    This converter processes PDFs page by page using GPT-4 Vision to:
    1. Understand complex layouts (tables, forms, multi-column)
    2. Preserve semantic structure and relationships
    3. Extract detailed technical information
    4. Handle scanned documents with OCR
    """

    def __init__(
        self,
        model: str = "gpt-4-vision-preview",
        max_tokens: int = 4000,
        detail: str = "high",
        dpi: int = 200,
    ):
        self.client = OpenAI()
        self.model = model
        self.max_tokens = max_tokens
        self.detail = detail
        self.dpi = dpi

    def convert(self, doc: LoadedPDF) -> str:
        """Convert PDF to Markdown using vision-language model analysis."""
        try:
            pdf_document = pymupdf.open(stream=doc.raw_bytes, filetype="pdf")

            # Process each page
            page_markdowns = []
            for page_num in range(len(pdf_document)):
                page_md = self._convert_page(pdf_document, page_num, doc.name)
                if page_md:
                    page_markdowns.append(page_md)

            # Combine pages with clear separators
            full_markdown = self._combine_pages(page_markdowns, doc.name)

            pdf_document.close()
            return full_markdown

        except Exception as e:
            logger.error(f"Error converting {doc.name}: {e}")
            # Fallback to basic conversion
            return self._fallback_convert(doc)

    def _convert_page(self, pdf_doc: pymupdf.Document, page_num: int, filename: str) -> str:
        """Convert a single page using vision analysis."""
        try:
            page = pdf_doc[page_num]

            # Render page as high-resolution image
            mat = pymupdf.Matrix(self.dpi / 72, self.dpi / 72)  # Scale matrix for DPI
            pix = page.get_pixmap(matrix=mat)
            img_data = pix.tobytes("png")
            pix = None  # Free memory

            # Convert to base64 for API
            img_b64 = base64.b64encode(img_data).decode()

            # Create specialized prompt based on filename/content type
            prompt = self._create_prompt(filename, page_num)

            # Call vision API
            response = self.client.chat.completions.create(
                model=self.model,
                messages=[
                    {
                        "role": "user",
                        "content": [
                            {"type": "text", "text": prompt},
                            {
                                "type": "image_url",
                                "image_url": {
                                    "url": f"data:image/png;base64,{img_b64}",
                                    "detail": self.detail
                                }
                            }
                        ]
                    }
                ],
                max_tokens=self.max_tokens,
                temperature=0.1,  # Low temperature for consistency
            )

            markdown_content = response.choices[0].message.content.strip()

            # Add page number comment for reference
            return f"<!-- Page {page_num + 1} -->\n\n{markdown_content}\n\n"

        except Exception as e:
            logger.warning(f"Failed to process page {page_num} of {filename}: {e}")
            return ""

    def _create_prompt(self, filename: str, page_num: int) -> str:
        """Create specialized prompts based on document type."""

        base_prompt = f"""Convert this PDF page to clean, semantic Markdown. Focus on:

                **CRITICAL REQUIREMENTS:**
                1. **Preserve ALL technical data** - numbers, specifications, pin names, values
                2. **Maintain relationships** - connect components to their specifications
                3. **Structure properly** - use appropriate headers (# ## ###)
                4. **Handle tables** - convert to proper Markdown table format
                5. **Extract forms/certificates** - capture all fields and values
                6. **OCR text accurately** - read all visible text including small print

                **SPECIFIC GUIDELINES:**
                - Use `**bold**` for important terms, component names, pin numbers
                - Use `|` tables for tabular data
                - Use `>` blockquotes for important notes/warnings
                - Use `- ` lists for specifications
                - Include units and exact values (e.g., "2.4 G – 2.5 G", "Pin ERS12K (31)")
                - For certificates: extract issuer, dates, equipment types, certificate numbers

                **OUTPUT FORMAT:**
                Pure Markdown only. No explanations or meta-commentary."""

        # Document-specific enhancements
        if "esps2wroom" in filename.lower() or "certificate" in filename.lower():
            base_prompt += """

**CERTIFICATE-SPECIFIC:**
- Extract certificate holder names exactly
- Capture all dates (issued, valid until)
- Note equipment types and model numbers
- Include certificate/approval numbers"""

        elif "hardware" in filename.lower() or "design" in filename.lower():
            base_prompt += """

**HARDWARE DESIGN-SPECIFIC:**
- Preserve pin assignments and numbers
- Maintain frequency ranges and specifications
- Include connection types (SPI, UART, etc.)
- Note resistor values and component references"""

        elif "datasheet" in filename.lower() or "technical" in filename.lower():
            base_prompt += """

**DATASHEET-SPECIFIC:**
- Preserve all electrical specifications
- Maintain memory sizes and storage values
- Include power mode descriptions
- Note voltage ranges and DAC specifications"""

        return base_prompt

    def _combine_pages(self, page_markdowns: List[str], filename: str) -> str:
        """Combine page markdowns into a coherent document."""

        # Create document header
        clean_name = filename.replace('.pdf', '').replace('-', ' ').replace('_', ' ').title()
        header = f"# {clean_name}\n\n"

        # Join pages
        content = "\n---\n\n".join(page_markdowns)

        return header + content

    def _fallback_convert(self, doc: LoadedPDF) -> str:
        """Fallback to basic PyMuPDF conversion if vision fails."""
        try:
            import pymupdf4llm
            pdf = pymupdf.open(stream=doc.raw_bytes, filetype="pdf")
            markdown = pymupdf4llm.to_markdown(pdf, page_chunks=False)
            pdf.close()
            return f"# {doc.name}\n\n{markdown}"
        except Exception as e:
            logger.error(f"Fallback conversion failed for {doc.name}: {e}")
            return f"# {doc.name}\n\nConversion failed."

import pymupdf
import pymupdf4llm
import fitz
from PIL import Image
import pytesseract
import io
import os
from spellchecker import SpellChecker
from agent import text_markdown_agent
from src.loader.types import LoadedPDF
from src.converter.base import PDFtoMarkdown
from src.agent.text_markdown_agent import TextToMarkdownAgent
from pathlib import Path
from typing import Optional


class PymuConverter(PDFtoMarkdown):
    def __init__(
        self,
        markup_dir,
        save_intermediate_pages=False,
        use_llm_refinement="basic_pymu",  # Changed default to basic_pymu
        overwrite_md_files=False,
    ):
        super().__init__()

        self.markup_dir = markup_dir
        self.save_intermediate_pages = save_intermediate_pages
        self.use_llm_refinement = use_llm_refinement
        self.overwrite_md_files = overwrite_md_files

        # Create mode-specific directories
        if self.use_llm_refinement == "basic_pymu":
            self.markup_dir = os.path.join(self.markup_dir, "basic_pymu")
        elif self.use_llm_refinement == "llm_refinement":
            self.markup_dir = os.path.join(self.markup_dir, "llm")
        elif self.use_llm_refinement == "no_llm_refinement":
            self.markup_dir = os.path.join(self.markup_dir, "nollm")
        else:
            print(f"Warning: Undefined processing mode {use_llm_refinement}, falling back to basic_pymu")
            self.use_llm_refinement = "basic_pymu"
            self.markup_dir = os.path.join(self.markup_dir, "basic_pymu")

        # Ensure directory exists
        Path(self.markup_dir).mkdir(parents=True, exist_ok=True)

        # Initialize text markdown agent if needed
        self.text_markdown_agent = TextToMarkdownAgent() if use_llm_refinement == "llm_refinement" else None

    def convert(self, doc: LoadedPDF) -> Optional[str]:
        """Main conversion method that processes a PDF document page by page."""
        try:
            if self.use_llm_refinement == "basic_pymu":
                # Use basic PyMuPDF conversion
                return self._handle_basic_conversion(doc)
            else:
                # Use advanced processing with or without LLM refinement
                return self.process_pdf_by_pages(doc)
        except Exception as e:
            print(f"Error processing PDF: {e}")
            return f"Error processing PDF: {e}"

    def _handle_basic_conversion(self, doc: LoadedPDF) -> str:
        """Handle basic PDF conversion using PyMuPDF."""
        pdf = pymupdf.open(stream=doc.raw_bytes, filetype="pdf")
        markdown = pymupdf4llm.to_markdown(pdf, page_chunks=False)
        pdf.close()
        # Check if markdown is empty or contains only whitespace
        if not markdown or not markdown.strip():
            return "No meaningful content found in PDF."
    
        # Save the converted markdown if requested
        if self.save_intermediate_pages:
            doc_name = Path(doc.name).stem
            output_path = os.path.join(self.markup_dir, f"{doc_name}.md")
            with open(output_path, "w") as f:
                f.write(markdown)

        return markdown

    def process_pdf_by_pages(self, doc: LoadedPDF) -> str:
        """Process each page of the PDF document using multiple methods."""
        # Open PDF with both libraries (for different extraction methods)
        pymupdf_doc = pymupdf.open(stream=doc.raw_bytes, filetype="pdf")
        fitz_doc = fitz.open(stream=doc.raw_bytes, filetype="pdf")
        doc_name = Path(doc.name).stem
        all_pages_text = ""

        try:
            # Process each page
            for page_num in range(len(fitz_doc)):
                page_file_path = os.path.join(
                    self.markup_dir, f"{doc_name}_page_{page_num}.md"
                )
                if not self.overwrite_md_files and os.path.exists(page_file_path):
                    print(f"Skipping page {page_file_path} as it already exists.")
                    with open(page_file_path, "r") as page_file:
                        page_md = page_file.read()
                else:
                    print(f"Processing page {page_file_path}.")
                    # Extract text using different methods
                    page_md = self.extract_text_from_page(
                        pymupdf_doc, fitz_doc, page_num
                    )

                    # Apply LLM refinement if enabled
                    if self.use_llm_refinement == "llm_refinement" and self.text_markdown_agent:
                        page_md = self.text_markdown_agent.text_to_markdown(page_md)

                    if self.save_intermediate_pages:
                        # Save page to file
                        with open(page_file_path, "w") as page_file:
                            page_file.write(page_md)

                all_pages_text += page_md
        finally:
            # Clean up
            pymupdf_doc.close()
            fitz_doc.close()

        return all_pages_text

    def extract_text_from_page(self, pymupdf_doc, fitz_doc, page_num):
        """Extract text from a page using multiple methods and combine them."""
        # Get text using PyMuPDF's native extraction
        pymupdf_text = self.extract_native_text(pymupdf_doc, page_num)

        # Get text using OCR
        fitz_page = fitz_doc[page_num]
        ocr_text = self.extract_ocr_text(fitz_page)

        # Extract tables using OCR
        table_text = self.extract_tables(fitz_page)
        if self.use_llm_refinement:
            # This section is needed as LLM can handle markdown formatting better
            # but the no llm mark down splitter is throwing away headders and making wrong sections so
            # we need the below section
            page_content = (
                f"# Page {page_num + 1}\n\n"
                f"## Text from PDF\n\n{pymupdf_text}\n\n"
                f"## OCR Text\n\n{ocr_text}\n\n"
                f"## Tables\n\n{table_text}\n\n"
                f"---\n\n"
            )
        else:
            page_content = (
                f"{pymupdf_text}\n\n"
                f"{ocr_text}\n\n"
                f"{table_text}\n\n"
                f"---Page {page_num + 1} \n\n"
            )
        return page_content

    def extract_native_text(self, pdf, page_num):
        """Extract text using PyMuPDF's native text extraction."""
        sub_doc = fitz.open()  # create empty document
        sub_doc.insert_pdf(pdf, from_page=page_num, to_page=page_num)
        markdown = pymupdf4llm.to_markdown(sub_doc)
        if markdown and markdown.strip():
            return markdown

    def extract_ocr_text(self, page):
        """Extract text from a page using OCR."""
        try:
            # Render page to image at 2x resolution for better OCR
            zoom = 2
            matrix = fitz.Matrix(zoom, zoom)
            pixmap = page.get_pixmap(matrix=matrix, alpha=False)

            # Convert to PIL image for OCR
            img_data = pixmap.tobytes("ppm")
            img = Image.open(io.BytesIO(img_data)).convert("L")

            # Run OCR
            ocr_text = pytesseract.image_to_string(img, lang="eng", config="--psm 12")

            # Clean up text
            ocr_text = self.clean_text(ocr_text)

            if ocr_text and ocr_text.strip():
                return ocr_text
            return "No text found via OCR"
        except Exception as e:
            return f"OCR failed: {str(e)}"

    def extract_tables(self, page):
        """Extract tables from a page using OCR and positional data."""
        try:
            # Render page to image
            zoom = 2
            matrix = fitz.Matrix(zoom, zoom)
            pixmap = page.get_pixmap(matrix=matrix, alpha=False)

            # Convert to PIL image
            img_data = pixmap.tobytes("ppm")
            img = Image.open(io.BytesIO(img_data)).convert("L")

            # Get positional data of text
            data = pytesseract.image_to_data(
                img, lang="eng", config="--psm 12", output_type=pytesseract.Output.DICT
            )

            # Build tables from positional data
            tables = self.build_tables_from_ocr_data(data)

            # Format tables as markdown
            formatted_tables = self.format_tables(tables)

            if formatted_tables and formatted_tables.strip():
                return formatted_tables
            return "No tables detected"
        except Exception as e:
            return f"Table extraction failed: {str(e)}"

    def build_tables_from_ocr_data(self, data):
        """Reconstruct tables from OCR positional data."""
        rows = []
        current_row = []
        last_y = None
        line_height_threshold = 10  # Adjust based on document

        # Group words into rows based on y-position
        for i in range(len(data["level"])):
            x = data["left"][i]
            y = data["top"][i]
            width = data["width"][i]
            height = data["height"][i]
            text = data["text"][i]

            if not text.strip():
                continue

            # New row if y-position is significantly different
            if last_y is None or abs(y - last_y) > line_height_threshold:
                if current_row:
                    rows.append(current_row)
                current_row = [text]
            else:
                current_row.append(text)

            last_y = y

        # Add the last row
        if current_row:
            rows.append(current_row)

        return rows

    def build_tables(self, data):
        """Reconstruct tables from OCR positional data."""
        tables = []
        n_boxes = len(data["level"])
        # Initialize a temporary list to hold words for table reconstruction
        current_row = []
        last_y = None

        for i in range(n_boxes):
            (x, y, w, h, word) = (
                data["left"][i],
                data["top"][i],
                data["width"][i],
                data["height"][i],
                data["text"][i],
            )

            if word.strip():
                # Check if the word is on the same line as the last word
                if last_y is None or abs(y - last_y) < 10:  # Adjust threshold as needed
                    current_row.append(word)
                else:
                    # If we hit a new line, save the current row and start a new one
                    tables.append(current_row)
                    current_row = [word]

                last_y = y

        # Append the last row if it exists
        if current_row:
            tables.append(current_row)
        formatted_tables = self.format_tables_as_markdown(tables)
        return formatted_tables

    def format_tables_as_markdown(self, tables):
        """Format detected tables as markdown tables."""
        if not tables or len(tables) < 2:  # Need at least header and one data row
            return ""

        # Use first row as header
        header = tables[0]
        if not header:
            return ""

        # Create markdown table
        md_table = "| " + " | ".join(header) + " |\n"
        md_table += "| " + " | ".join(["---"] * len(header)) + " |\n"

        # Add data rows
        for row in tables[1:]:
            # Ensure row has same number of columns as header
            while len(row) < len(header):
                row.append("")

            # Truncate if too long
            row = row[: len(header)]

            md_table += "| " + " | ".join(row) + " |\n"

        return md_table

    def format_tables(self, tables):
        formatted = ""
        for table in tables:
            formatted += " ".join(table) + "\n"
        return formatted

    def clean_text(self, text):
        """Clean extracted text."""
        # Spell check did not imporve and remove important cues
        # Remove excessive newlines
        # text = text.replace("\n\n", "\n")
        # Did not help
        # Remove excessive spaces
        text = text.replace("  ", " ")
        return text.strip()

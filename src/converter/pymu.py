import pymupdf
import pymupdf4llm

from src.loader.types import LoadedPDF
from src.converter.base import PDFtoMarkdown
import fitz
from PIL import Image
import pytesseract
import io
from spellchecker import SpellChecker


class PymuConverter(PDFtoMarkdown):
    def __init__(self):
        super().__init__()

    def convert(self, doc: LoadedPDF) -> str:
        try:
            # First try pymupdf4llm's markdown conversion
            markdown = self._handle_normal_pdf(doc)
            if markdown and markdown.strip():
                return markdown

            # If no meaningful content, try OCR
            return self._handle_scanned_pdf_enhanced(doc)  # TODO: this is a hack

        except Exception as e:
            # If pymupdf4llm fails, try OCR
            return self._handle_scanned_pdf(doc)

    # ────────────────────────────────────────────────────────────────
    def _handle_normal_pdf(self, doc: LoadedPDF) -> str:
        pdf = pymupdf.open(stream=doc.raw_bytes, filetype="pdf")
        markdown = pymupdf4llm.to_markdown(pdf, page_chunks=False)
        pdf.close()
        return markdown

    # ────────────────────────────────────────────────────────────────
    def _handle_scanned_pdf_enhanced(self, doc: LoadedPDF) -> str:
        zoom = 2  # 2x resolution for better OCR
        mat = fitz.Matrix(zoom, zoom)
        pdf = fitz.open(stream=doc.raw_bytes, filetype="pdf")
        table_seperator = "===================Tables=============================\n\n"
        page_seperator = "===================End Page===========================\n\n"

        text = ""
        # To store reconstructed tables
        breakpoint()
        for page_number, page in enumerate(pdf[0:10]):
            tables = []
            table_seperator = (
                f"=================== Tables =============================\n\n"
            )
            page_seperator = f"===================End Page-{page_number}===========================\n\n"

            page_text = ""
            pix = page.get_pixmap(matrix=mat, alpha=False)
            img = Image.open(io.BytesIO(pix.tobytes("ppm"))).convert("L")

            # Use OCR to extract text
            page_text = pytesseract.image_to_string(
                img, lang="eng", config="--psm 6"
            )  # Use psm 6 for block of text
            text += page_text + "\n\n" + table_seperator

            # Get word positions for further processing
            data = pytesseract.image_to_data(
                img, lang="eng", config="--psm 12", output_type=pytesseract.Output.DICT
            )
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
                    if (
                        last_y is None or abs(y - last_y) < 10
                    ):  # Adjust threshold as needed
                        current_row.append(word)
                    else:
                        # If we hit a new line, save the current row and start a new one
                        tables.append(current_row)
                        current_row = [word]

                    last_y = y

            # Append the last row if it exists
            if current_row:
                tables.append(current_row)
            formatted_tables = self.format_tables(tables)
            formatted_tables = self.clean_text(formatted_tables)
            text += formatted_tables + page_seperator
        pdf.close()
        # Optionally, format the tables into a string or another structure

        return text

    def format_tables(self, tables):
        formatted = ""
        for table in tables:
            formatted += " ".join(table) + "\n"
        return formatted

    def _handle_scanned_pdf_enhanced_v2(self, doc: LoadedPDF) -> str:
        zoom = 2  # 2x resolution
        mat = fitz.Matrix(zoom, zoom)
        pdf = fitz.open(stream=doc.raw_bytes, filetype="pdf")
        text = ""
        for page in pdf:
            pix = page.get_pixmap(matrix=mat, alpha=False)
            img = Image.open(io.BytesIO(pix.tobytes("ppm"))).convert("L")
            text += (
                pytesseract.image_to_string(
                    img,
                    lang="eng",
                    config="--psm 12",
                    output_type=pytesseract.Output.DICT,
                )
                + "\n\n"
            )

        data = pytesseract.image_to_data(
            img, lang="eng", config="--psm 12", output_type=pytesseract.Output.DICT
        )
        n_boxes = len(data["level"])
        for i in range(n_boxes):
            (x, y, w, h, text) = (
                data["left"][i],
                data["top"][i],
                data["width"][i],
                data["height"][i],
                data["text"][i],
            )
            if text.strip():
                print(f"Word: {text} at ({x},{y},{w},{h})")

        pdf.close()
        # breakpoint()
        return text

    # ────────────────────────────────────────────────────────────────
    def filter_non_words(self, text: str) -> str:
        spell = SpellChecker()
        words = text.split()
        filtered = [w for w in words if w.lower() in spell or len(w) <= 2]
        return " ".join(filtered)

    def clean_text(self, text: str) -> str:
        # remove all newlines
        # text = self.filter_non_words(text)

        text = text.replace("\n", " ")
        # remove all double spaces
        text = text.replace("  ", " ")
        return text

    # ────────────────────────────────────────────────────────────────
    # TODO: this is a hack to get the text from a scanned PDF
    # it should be replaced with a more robust OCR solution
    def _handle_scanned_pdf(self, doc: LoadedPDF) -> str:
        text = ""
        pdf = fitz.open(stream=doc.raw_bytes, filetype="pdf")
        try:
            for page in pdf:
                # Get the page as an image
                # get_pixmap() requires alpha parameter
                pix = page.get_pixmap(alpha=False)

                # Convert PyMuPDF pixmap to PIL Image (using tuple for size)
                img = Image.frombytes("RGB", (pix.width, pix.height), pix.samples)

                # Use OCR to extract text
                text += pytesseract.image_to_string(img) + "\n\n"
        finally:
            pdf.close()
        breakpoint()
        return text

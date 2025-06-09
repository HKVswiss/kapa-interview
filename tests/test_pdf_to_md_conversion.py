import sys
import os

# Add the parent directory of the current file to sys.path
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))

from src.converter.pymu import PymuConverter
from src.loader.types import LoadedPDF
import os
import unittest


class TestPDFToMarkdownConversion(unittest.TestCase):

    def setUp(self):
        self.test_pdf_path = "data/pdfs/esp8266_hardware_design_guidelines.pdf"  # Change this to your actual PDF file name
        self.converter = PymuConverter()

    def test_conversion(self):
        with open(self.test_pdf_path, "rb") as f:
            raw_bytes = f.read()

        doc = LoadedPDF(name=os.path.basename(self.test_pdf_path), raw_bytes=raw_bytes)
        markdown = self.converter.convert(doc)

        output_file_path = "output_markdown.txt"
        with open(output_file_path, "w") as output_file:
            output_file.write(markdown)

        # expected_content = "Expected content from your PDF goes here."  # Update this with the expected output
        # self.assertEqual(markdown.strip(), expected_content.strip())


if __name__ == "__main__":
    unittest.main()

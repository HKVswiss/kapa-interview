import sys
import os


sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))

from src.converter.pymu_hybrid_withpages import PymuConverter
from src.loader.types import LoadedPDF
import os
import unittest


class TestPDFToMarkdownConversion(unittest.TestCase):

    def setUp(self):
        # Change this to your actual PDF file name

        self.test_pdf_path = "data/pdfs/21098-ESPS2WROOM-scan.pdf"
        markup_dir = "data/processed_pages"
        self.converter = PymuConverter(
            markup_dir,
            save_intermediate_pages=True,
            use_llm_refinement=True,
            overwrite_md_files=False,
        )

    def test_conversion(self):
        with open(self.test_pdf_path, "rb") as f:
            raw_bytes = f.read()

        doc = LoadedPDF(name=os.path.basename(self.test_pdf_path), raw_bytes=raw_bytes)
        markdown = self.converter.convert(doc)

        output_file_path = "output_markdown.txt"
        with open(output_file_path, "w") as output_file:
            output_file.write(markdown)


if __name__ == "__main__":
    unittest.main()

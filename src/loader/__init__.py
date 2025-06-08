"""
PDF Loading Package

This package contains classes for loading PDF files from various sources.

Classes:
    DirectoryPDFLoader: Load all PDF files from a directory
    LoadedPDF: Data structure representing a loaded PDF file

Usage:
    from src.loader import DirectoryPDFLoader, LoadedPDF

    loader = DirectoryPDFLoader("path/to/pdfs")
    for pdf_doc in loader.load():
        print(f"Loaded: {pdf_doc.name}")
"""

from src.loader.pdf_loader import DirectoryPDFLoader
from src.loader.types import LoadedPDF

__all__ = [
    "DirectoryPDFLoader",
    "LoadedPDF",
]

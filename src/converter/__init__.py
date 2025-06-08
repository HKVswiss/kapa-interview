"""
PDF to Markdown Converter Package

Basic Converters:
    PymuConverter: Basic PyMuPDF conversion
    PDFtoMarkdown: Abstract base class

Advanced Converters (optional):
    LLMVisionConverter: GPT-4 Vision-based conversion
    HybridOCRConverter: PyMuPDF + OCR hybrid
    EnhancedPyMuConverter: Enhanced PyMuPDF with post-processing

Factory:
    ConverterFactory: Factory for creating converters
    ConverterType: Enum of available converter types

Usage:
    from src.converter import ConverterFactory, ConverterType

    # Get best available converter
    converter = ConverterFactory.get_best()

    # Or create specific converter
    converter = ConverterFactory.create(ConverterType.VISION)
"""

# Core converters (always available)
from src.converter.base import PDFtoMarkdown
from src.converter.pymu import PymuConverter


__all__ = [
    "PDFtoMarkdown",
    "PymuConverter",
]

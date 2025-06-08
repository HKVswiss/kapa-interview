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
from src.converter.factory import ConverterFactory, ConverterType

__all__ = [
    "PDFtoMarkdown",
    "PymuConverter",
    "ConverterFactory",
    "ConverterType",
]

# Optional advanced converters
try:
    from src.converter.llm_vision_converter import LLMVisionConverter
    __all__.append("LLMVisionConverter")
except ImportError:
    pass

try:
    from src.converter.hybrid_ocr_converter import HybridOCRConverter
    __all__.append("HybridOCRConverter")
except ImportError:
    pass

try:
    from src.converter.enhanced_pymu_converter import EnhancedPyMuConverter
    __all__.append("EnhancedPyMuConverter")
except ImportError:
    pass

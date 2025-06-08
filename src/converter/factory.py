"""
PDF to Markdown Converter Factory

Simple factory for creating different PDF converters.
"""

import logging
import os
from enum import Enum
from typing import Optional, Dict, Any

from src.converter.base import PDFtoMarkdown
from src.converter.pymu import PymuConverter

logger = logging.getLogger(__name__)


class ConverterType(Enum):
    """Available converter types."""
    BASIC = "basic"
    ENHANCED = "enhanced"
    OCR = "ocr"
    VISION = "vision"


class ConverterFactory:
    """Factory for creating PDF converters."""

    @staticmethod
    def create(converter_type: ConverterType, **options) -> PDFtoMarkdown:
        """Create a converter instance."""

        if converter_type == ConverterType.BASIC:
            return PymuConverter()

        elif converter_type == ConverterType.ENHANCED:
            try:
                from src.converter.enhanced_pymu_converter import EnhancedPyMuConverter
                return EnhancedPyMuConverter(**options)
            except ImportError:
                logger.warning("Enhanced converter not available, using basic")
                return PymuConverter()

        elif converter_type == ConverterType.OCR:
            try:
                from src.converter.hybrid_ocr_converter import HybridOCRConverter
                return HybridOCRConverter(**options)
            except ImportError:
                logger.warning("OCR converter not available, using enhanced")
                return ConverterFactory.create(ConverterType.ENHANCED)

        elif converter_type == ConverterType.VISION:
            try:
                from src.converter.llm_vision_converter import LLMVisionConverter
                return LLMVisionConverter(**options)
            except ImportError:
                logger.warning("Vision converter not available, using OCR")
                return ConverterFactory.create(ConverterType.OCR)

        raise ValueError(f"Unknown converter type: {converter_type}")

    @staticmethod
    def get_best() -> PDFtoMarkdown:
        """Get the best available converter."""

        # Try vision first if OpenAI key available
        if os.getenv("OPENAI_API_KEY"):
            try:
                return ConverterFactory.create(ConverterType.VISION)
            except Exception:
                pass

        # Try OCR if tesseract available
        try:
            import pytesseract
            pytesseract.get_tesseract_version()
            return ConverterFactory.create(ConverterType.OCR)
        except Exception:
            pass

        # Fallback to enhanced or basic
        try:
            return ConverterFactory.create(ConverterType.ENHANCED)
        except Exception:
            return ConverterFactory.create(ConverterType.BASIC)

    @staticmethod
    def list_available() -> Dict[ConverterType, bool]:
        """List available converters."""
        return {
            converter_type: _try_create(converter_type)
            for converter_type in ConverterType
        }


def _try_create(converter_type: ConverterType) -> bool:
    """Check if converter can be created."""
    try:
        ConverterFactory.create(converter_type)
        return True
    except Exception:
        return False


# Keep old names for compatibility
create_converter = ConverterFactory.create
get_recommended_converter = ConverterFactory.get_best
list_available_converters = ConverterFactory.list_available

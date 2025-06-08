"""
Kapa PDF RAG System

PDF to Markdown conversion and RAG system for technical documents.

Quick Start:
    from src import RAGAgent, ConverterFactory

    # Auto-select best converter
    converter = ConverterFactory.get_best()

    # Create RAG agent
    agent = RAGAgent(
        loader=DirectoryPDFLoader("pdfs/"),
        converter=converter,
        chunker=MarkdownSectionChunker(),
        store=InMemoryVectorStore()
    )

    # Index and ask questions
    agent.index()
    answer, sources = agent.answer("What is the frequency range?")
"""

# Main components
from .agent.rag_agent import RAGAgent
from .converter.factory import ConverterFactory
from .loader.pdf_loader import DirectoryPDFLoader
from .chunker.markdown_section_chunker import MarkdownSectionChunker
from .vector_store.in_memory import InMemoryVectorStore

# Common types
from src.loader.types import LoadedPDF
from src.chunker.types import Chunk
from src.agent.types import Document

# Base classes
from src.converter.base import PDFtoMarkdown
from src.converter.pymu import PymuConverter
from src.chunker.base import BaseChunker

__all__ = [
    # Core RAG
    "RAGAgent",
    "ConverterFactory",

    # Components
    "DirectoryPDFLoader",
    "MarkdownSectionChunker",
    "InMemoryVectorStore",

    # Types
    "LoadedPDF",
    "Chunk",
    "Document",

    # Base classes
    "PDFtoMarkdown",
    "PymuConverter",
    "BaseChunker",
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

# Version info
__version__ = "0.1.0"
__author__ = "Kapa.ai"
__email__ = "engineering@kapa.ai"

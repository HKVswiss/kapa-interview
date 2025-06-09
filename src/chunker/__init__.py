"""
Text Chunking Package

This package contains classes for splitting Markdown text into semantic chunks
for vector storage and retrieval.

Classes:
    BaseChunker: Abstract base class for all chunkers
    MarkdownSectionChunker: Chunks markdown by sections and headings
    Chunk: Data structure representing a text chunk

Usage:
    from src.chunker import MarkdownSectionChunker, Chunk

    chunker = MarkdownSectionChunker(max_chunk_size=2000)
    chunks = chunker.split(markdown_text)
"""

from src.chunker.base import BaseChunker
from src.chunker.markdown_section_chunker import MarkdownSectionChunker
from src.chunker.types import Chunk

__all__ = [
    "BaseChunker",
    "MarkdownSectionChunker",
    "Chunk",
]

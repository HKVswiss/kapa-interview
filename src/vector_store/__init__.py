"""
Vector Store Package

This package contains classes for storing and searching document embeddings.

Classes:
    InMemoryVectorStore: In-memory vector storage using OpenAI embeddings

Usage:
    from src.vector_store import InMemoryVectorStore

    store = InMemoryVectorStore()
    store.add_texts(["text1", "text2", "text3"])
    results = store.search("search query", k=3)
"""

from src.vector_store.in_memory import InMemoryVectorStore

__all__ = [
    "InMemoryVectorStore",
]

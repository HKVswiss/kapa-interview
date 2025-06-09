"""
RAG Agent Package

This package contains the main RAG (Retrieval-Augmented Generation) agent
that orchestrates the PDF processing pipeline.

Classes:
    RAGAgent: Main orchestrator for PDF indexing and question answering
    Document: Data structure representing a processed PDF document

Usage:
    from src.agent import RAGAgent, Document
    
    agent = RAGAgent(loader, converter, chunker, store)
    agent.index()
    answer, sources = agent.answer("Your question here")
"""

from src.agent.rag_agent import RAGAgent
from src.agent.types import Document

__all__ = [
    "RAGAgent",
    "Document",
] 
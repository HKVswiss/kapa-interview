#!/usr/bin/env python3
"""
Setup script for Kapa PDF RAG system.
"""

from setuptools import setup, find_namespace_packages

# Read requirements from file
with open("requirements.txt") as f:
    requirements = f.read().splitlines()

setup(
    name="kapa-pdf-rag",
    version="0.1.0",
    packages=find_namespace_packages(where="src", include=["*"]),
    install_requires=requirements,
    python_requires=">=3.8",
)

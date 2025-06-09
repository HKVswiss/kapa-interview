# Quick Installation

Create a Python virtual environment:

```bash
python -m venv venv
```

Use the provided Make commands:

```bash
make docker-build
make docker-up
make docker-run
```

# Streamlit App

The following inputs are available in the Streamlit app:

- **top_k**: Number of chunks to retrieve in the RAG system.
- **pdf_to_markdown conversion modes**: PDF to Markdown conversion can be performed using the following modes:
  - `basic_pymu`
  - `no_llm_refinement`
  - `llm_refinement`
- **over_write_existing_files**: Overwrites previously created Markdown files and regenerates them.

## Important Files

- Questions are located in `Questions.md`.
- Solutions and thought processes are documented in:
  - `problems_thoughprocess.md`
  - `problems_thoughprocess.txt`

# Repository Branches

The repository contains four branches:

- **basic setup**: Initial provided code.
- **intermediate-solution**: Contains basic OCR setup.
- **clean-markdown** *(final solution)*:
  - Combines PyMu reader, Fitz (OCR), and LLM rendering.
  - Detailed explanation available in `problems_thoughprocess.md`.
- **main**: Merged with `clean-markdown`.

Additionally, to compare `main` with the basic setup, a new branch `merge-main-into-basic` has been created, and a pull request is available for review.


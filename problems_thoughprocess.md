# PDF Processing and RAG System Development Process

## Initial Problems Identified

1. Scanned documents were not being processed
2. Images were not being processed at all
3. Table formatting was not human-readable
4. Page numbers were missing in the output

## Solution Development Process

### Initial Thought Process

1. Realized this is not a real-time application, allowing for:
   - Multiple PDF readers for different content types (text, tables, images)
   - Page-level ensemble approach for consolidated markdown
2. Potential use of LLM for iterative consolidation
3. Exploration of GPT-4.1's multi-modal capabilities for image-related queries

### Major Problems and Solutions

#### 1. Scanned Document Processing

**Problem:**
- Scanned documents (e.g., `21098-ESPS2WROOM-scan.pdf`) were completely unreadable
- Initial implementation using `pymupdf` and `pymupdf4llm` ignored scanned content:
```python
pdf = pymupdf.open(stream=doc.raw_bytes, filetype="pdf")
markdown = pymupdf4llm.to_markdown(pdf, page_chunks=False)
```

**Solution:**
- Implemented hybrid approach using both `pymupdf` and `fitz` packages
- `pymupdf` for processing plain text and creating headings
- `fitz` for handling scanned content and basic table detection
- Better chunking strategy for improved retrieval

#### 2. Hybrid PDF to Markdown Converter

**Implementation:**
For each page, the system:
1. Uses `pymupdf` for paragraph extraction
2. Uses `fitz` for table extraction
3. Aligns and combines text from both sources
4. Uses LLM for markdown formatting refinement
5. Stores processed files in `data/processed_pages/llm`

**Benefits:**
- Human-readable markdown format
- Better structure preservation
- Improved table handling

#### 3. Retrieval Performance

**Problem:**
- Some queries failed despite available information (e.g., "maximum storage temperature for EFM8BB3")
- Table information was particularly challenging to retrieve

**Solution:**
- Increased `top_k` parameter from 3 to 5 for better context retrieval
- Improved chunking strategy to maintain table context

### UI Improvements

Added two key controls in Streamlit interface:
1. "Number of chunks to retrieve" selector
   - Controls `top_k` parameter in RAG system
   - Range: 1-10 chunks
   - Default: 5 chunks

2. "Use LLM Refinement" toggle
   - Enables/disables LLM refinement of PDF extraction
   - Affects output quality vs processing speed
   - Results stored in separate directories (`llm/` vs `nollm/`)

## Results

The final system successfully:
- Processes both regular and scanned PDFs
- Preserves table structures
- Maintains proper document formatting
- Provides flexible retrieval options
- Allows for LLM-based refinement when needed

## Future Improvements

Potential areas for enhancement:
1. Image processing capabilities
2. More sophisticated table detection
3. Optimization of LLM refinement process
4. Enhanced chunking strategies for special content types

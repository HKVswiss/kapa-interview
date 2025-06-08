from pathlib import Path

import streamlit as st

from src.agent.rag_agent import RAGAgent
from src.chunker.markdown_section_chunker import MarkdownSectionChunker

# from src.converter.factory import ConverterFactory, ConverterType

# from src.converter.pymu import PymuConverter
from src.converter.pymu_hybrid_withpages import PymuConverter
from src.loader.pdf_loader import DirectoryPDFLoader
from src.vector_store.in_memory import InMemoryVectorStore

DATA_DIR = Path(__file__).parent.parent / "data" / "pdfs"
# DATA_DIR = Path(__file__).parent.parent / "data" / "pdfs_guidelines"
# DATA_DIR = Path(__file__).parent.parent / "data" / "pdfs_datasheet"
# /home/harivydana/Interview/Kaiko/kapa-interview/data/pdfs_datasheet_/efm8bb3-datasheet.pdf
markup_dir = Path(__file__).parent.parent / "data" / "processed_pages"
print(f"Using data directory: {markup_dir}")
# ────────────────────────────────────────────────────────────────
# Page config (browser-tab title stays constant)
# ────────────────────────────────────────────────────────────────
st.set_page_config(page_title="Chat over PDFs", layout="wide")


# ────────────────────────────────────────────────────────────────
# Session-state defaults
# ────────────────────────────────────────────────────────────────
if "use_llm_refinement" not in st.session_state:
    st.session_state.use_llm_refinement = False
use_llm_refinement = st.session_state.use_llm_refinement

if "top_k" not in st.session_state:
    st.session_state.top_k = 5

if "mode" not in st.session_state:
    st.session_state.mode = "Browse"

# Initialize agent first
# Initialize or reinitialize agent based on settings
should_reinit = (
    "agent" not in st.session_state
    or st.session_state.agent.converter.use_llm_refinement != use_llm_refinement
    or st.session_state.agent.top_k != st.session_state.top_k
)

if should_reinit:
    st.session_state.agent = RAGAgent(
        loader=DirectoryPDFLoader(DATA_DIR),
        converter=PymuConverter(
            markup_dir,
            save_intermediate_pages=True,
            use_llm_refinement=use_llm_refinement,
            overwrite_md_files=False,
        ),
        chunker=MarkdownSectionChunker(),
        store=InMemoryVectorStore(),
        top_k=st.session_state.top_k,
    )

agent = st.session_state.agent

# ────────────────────────────────────────────────────────────────
# Sidebar
# ────────────────────────────────────────────────────────────────
with st.sidebar:
    # Index/Reset section (at the top)
    if "index_msg" in st.session_state:
        st.success(st.session_state.index_msg)
        del st.session_state.index_msg

    # Index / reset actions - First row
    if agent.docs:
        if st.button("♻️ Reset index", use_container_width=True):
            st.session_state.agent = RAGAgent(
                loader=DirectoryPDFLoader(DATA_DIR),
                converter=PymuConverter(
                    markup_dir,
                    save_intermediate_pages=True,
                    use_llm_refinement=use_llm_refinement,
                    overwrite_md_files=False,
                ),
                chunker=MarkdownSectionChunker(),
                store=InMemoryVectorStore(),
                top_k=st.session_state.top_k,
            )
            st.session_state.mode = "Browse"
            st.rerun()
    else:
        if st.button("📄 Load & index PDFs", use_container_width=True):
            agent.index()
            st.session_state.index_msg = f"Indexed {len(agent.docs)} PDF(s)"
            st.session_state.mode = "Browse"
            st.rerun()

    if not agent.docs:
        st.info("Index some PDFs first.")

    if st.button("📚 Browse", key="nav_browse", use_container_width=True):
        st.session_state.mode = "Browse"
    if st.button("💬 Chat", key="nav_chat", use_container_width=True):
        st.session_state.mode = "Chat"

    st.markdown("---")

    # Settings section - Third row
    st.markdown("### Settings")

    # top_k selection
    top_k = st.selectbox(
        "Number of chunks to retrieve",
        options=list(range(1, 11)),
        index=st.session_state.top_k - 1,
        help="Select the number of top chunks to retrieve for answering queries.",
    )
    st.session_state.top_k = top_k

    # LLM refinement checkbox
    st.session_state.use_llm_refinement = st.checkbox(
        "🤖 Use LLM Refinement",
        value=st.session_state.use_llm_refinement,
        help="If enabled, GPT-based cleanup will refine the converted Markdown from PDFs.",
    )

# ────────────────────────────────────────────────────────────────
# Dynamic page title (rendered *after* sidebar)
# ────────────────────────────────────────────────────────────────
if st.session_state.mode == "Chat":
    st.title("💬 Chat over indexed PDFs")
else:
    st.title("📚 Browse indexed PDFs")

# ────────────────────────────────────────────────────────────────
# Mode A: Chat
# ────────────────────────────────────────────────────────────────
if st.session_state.mode == "Chat":
    if not agent.docs:
        st.info("Index some PDFs first.")
    else:
        # 🆕 Explanation of how Chat works
        st.info(
            "When you ask a question, the app first **retrieves** the most chunks from the indexed PDFs "
            "sections using semantic search, then it **generates** an answer from those "
            "top-ranked chunks.\n\n"
            "* The assistant's answer appears above.\n"
            "* The exact chunks that were used are listed underneath."
        )

        query = st.chat_input("Ask a question …")

        if query:
            answer, chunks = agent.answer(query)
            st.chat_message("user").markdown(query)
            st.chat_message("assistant").markdown(answer)

            if chunks:
                sources_md = "\n\n---\n\n".join(
                    f"**Chunk {i+1} (score ≈ {score:.4f})**\n\n{chunk}"
                    for i, (chunk, score) in enumerate(chunks)
                )
                st.markdown(f"---\n\n### Source chunks\n\n{sources_md}")

# ────────────────────────────────────────────────────────────────
# Mode B: Browse converted Markdown
# ────────────────────────────────────────────────────────────────
else:
    if not agent.docs:
        st.info("Index some PDFs first.")
    else:
        st.info(
            "This view lets you inspect the output of the PDF→Markdown conversion **and** "
            "see how that Markdown was chunked for retrieval:\n\n"
            "• **View Markdown** – full converted document.\n\n"
            "• **View Chunks** – the smaller sections the chat engine actually searches."
        )

        fname = st.selectbox(
            "Select a document",
            list(agent.docs.keys()),
            key="doc_select",
        )
        doc = agent.docs[fname]

        with st.expander("View Markdown", expanded=False):
            st.markdown(doc.markdown)

        with st.expander("View Chunks", expanded=False):
            chunk_string = "\n\n---\n\n".join([c.content for c in doc.chunks])
            st.markdown(chunk_string)

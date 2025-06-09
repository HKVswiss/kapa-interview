import re
from typing import Optional
import os
from urllib import response
from agents import Agent, Runner, RunConfig, ModelSettings, function_tool
from pydantic import BaseModel, Field, PrivateAttr
import asyncio


MODEL_CHOICE = "gpt-4.1-mini-2025-04-14"
LLM_TEMPERATURE = 0.0


class MarkDown_Text(BaseModel):
    """generate markdown text for the whole page."""

    markdown_text: str = None


class TextToMarkdownAgent:
    """
    Agent that takes a plain text file as input and converts it to a markdown file.
    """

    def __init__(self):
        self.messages = []
        self.agent = Agent(
            name="text_to_markdown",
            model=MODEL_CHOICE,
            model_settings=ModelSettings(temperature=LLM_TEMPERATURE),
            instructions=(
                "You are a helpful assistant responsible for converting PDF content into a clean and structured markdown format.\n\n"
                "### Context:\n"
                "- The PDF content has been extracted using three different methods:\n"
                "  1. **Direct PDF text extraction** – reliable for plain text.\n"
                "  2. **OCR (Optical Character Recognition)** – used for scanned content, images, and some embedded tables.\n"
                "  3. **Table reconstruction via OCR** – used to accurately recover and format tabular data.\n\n"
                "### Instructions:\n"
                "- The extracted content may contain redundancy across the methods.\n"
                "- Identify and **deduplicate** overlapping or repeated information.\n"
                "- Ensure that **tables are correctly placed** and rendered in proper markdown format.\n"
                "- Your input will be structured per page as follows:\n\n"
                "```\n"
                "# Page {page_num + 1}\n\n"
                "## Text from PDF\n\n"
                "pymupdf_text\n\n"
                "## OCR Text\n\n"
                "ocr_text\n\n"
                "## Tables\n\n"
                "table_text\n\n"
                "---\n"
                "```\n"
                "- Generate a single consolidated markdown output for each page.\n"
                "- Keep the final result clean, well-formatted, and human-readable.\n"
                "- include page numbers in the markdown output at the bottom of the page.\n"
                "- Ensure it is optimized for downstream processing by a RAG (Retrieval-Augmented Generation) system.\n"
            ),
            output_type=MarkDown_Text,
        )

    async def run(self):
        response = await Runner.run(self.agent, input=self.messages)
        output = response.final_output.markdown_text
        return output

    def text_to_markdown(self, text: str) -> str:
        # in future if this is critical i can also add context of past pages

        self.messages = []
        self.add_message(role="system", content=text)
        output = asyncio.run(self.run())
        return output

    def add_message(self, role: str, content: str) -> None:
        """Add a message to the context's message history."""
        self.messages.append({"role": role, "content": content})
        return


# Example usage:
# agent = TextToMarkdownAgent('input.txt')
# agent.convert()

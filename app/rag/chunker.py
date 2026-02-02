from langchain_text_splitters import RecursiveCharacterTextSplitter


def chunk_documents(pages, chunk_size: int = 800, chunk_overlap: int = 100):
    """
    Split GST documents into semantically meaningful chunks.

    Returns:
        List[dict] with keys:
        - content
        - page
    """

    splitter = RecursiveCharacterTextSplitter(
        chunk_size=chunk_size,
        chunk_overlap=chunk_overlap,
        separators=["\n\n", "\n", " ", ""],
    )

    chunks = []

    for page in pages:
        page_number = page.metadata.get("page", None)
        texts = splitter.split_text(page.page_content)

        for text in texts:
            chunks.append(
                {
                    "content": text.strip(),
                    "page": page_number,
                }
            )

    return chunks


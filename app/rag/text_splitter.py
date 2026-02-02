from langchain.text_splitter import RecursiveCharacterTextSplitter

def split_documents(pages):
    splitter = RecursiveCharacterTextSplitter(
        chunk_size=500,
        chunk_overlap=50
    )

    chunks = []
    docs = splitter.split_documents(pages)

    for d in docs:
        chunks.append({
            "content": d.page_content,
            "page": d.metadata.get("page", 0),
            "source": d.metadata.get("source", "")
        })

    return chunks

from app.rag.pinecone_client import get_or_create_index
from app.rag.pdf_loader import load_pdf
from app.rag.chunker import chunk_documents
from app.rag.embedder import embed_text

BATCH_SIZE = 1000


def index_gst_pdf(pdf_path: str) -> int:
    index = get_or_create_index()

    pages = load_pdf(pdf_path)
    chunks = chunk_documents(pages)

    vectors = []

    for i, chunk in enumerate(chunks):
        embedding = embed_text(chunk["content"])

        vectors.append(
            {
                "id": f"gst-{i}",
                "values": embedding,
                "metadata": {
                    "source": "gst_pdf",
                    "page": chunk["page"],
                    "text": chunk["content"][:1000],  # metadata limit safety
                },
            }
        )

    # 🔥 BATCHED UPSERT (CRITICAL)
    for i in range(0, len(vectors), BATCH_SIZE):
        batch = vectors[i : i + BATCH_SIZE]
        index.upsert(batch)

    return len(vectors)

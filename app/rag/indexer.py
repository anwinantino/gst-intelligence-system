from typing import List, Dict

from app.rag.embeddings import get_embedding_model
from app.rag.pinecone_client import get_pinecone_client
from app.core.config import settings


def index_chunks(chunks: List[Dict[str, str]]) -> None:
    """
    Index GST document chunks into Pinecone.

    Each chunk must have:
    {
        "content": str,
        "source": str,
        "section": str
    }
    """

    # Initialize clients
    embedder = get_embedding_model()
    pinecone = get_pinecone_client()
    index = pinecone.Index(settings.pinecone_index_name)

    vectors = []

    for idx, chunk in enumerate(chunks):
        # Generate embedding (HuggingFace sentence-transformers)
        embedding = embedder.encode(
            chunk["content"],
            normalize_embeddings=True
        ).tolist()

        vectors.append(
            {
                "id": f"gst-{idx}",
                "values": embedding,
                "metadata": {
                    "source": chunk["source"],
                    "section": chunk["section"],
                    "text": chunk["content"],
                },
            }
        )

    # Upsert into Pinecone
    index.upsert(vectors=vectors)

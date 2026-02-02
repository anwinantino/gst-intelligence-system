from app.rag.pinecone_client import get_pinecone_index
from app.rag.embeddings import get_embedding_model


def retrieve_gst_context(query: str, top_k: int = 5):
    index = get_pinecone_index()
    embedder = get_embedding_model()

    vector = embedder.embed_query(query)

    results = index.query(
        vector=vector,
        top_k=top_k,
        include_metadata=True,
    )

    return results["matches"]
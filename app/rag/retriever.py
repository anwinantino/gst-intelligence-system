from app.rag.pinecone_client import get_or_create_index
from app.rag.embedder import embed_text


def retrieve_gst_context(query: str, top_k: int = 5) -> list[dict]:
    """
    Retrieve relevant GST chunks from Pinecone.
    """

    index = get_or_create_index()
    query_vector = embed_text(query)

    results = index.query(
        vector=query_vector,
        top_k=top_k,
        include_metadata=True,
    )

    matches = []

    for match in results.get("matches", []):
        metadata = match.get("metadata", {})
        matches.append(
            {
                "text": metadata.get("text", ""),
                "page": metadata.get("page"),
                "score": match.get("score"),
            }
        )

    return matches

from sentence_transformers import SentenceTransformer

# Load once (IMPORTANT for performance)
_model = SentenceTransformer("sentence-transformers/all-MiniLM-L6-v2")


def embed_text(text: str) -> list[float]:
    """
    Generate a normalized embedding for a single text chunk.

    - Deterministic
    - No external API calls
    - Pinecone-compatible
    """

    embedding = _model.encode(
        text,
        normalize_embeddings=True,
    )

    return embedding.tolist()

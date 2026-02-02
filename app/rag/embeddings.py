from sentence_transformers import SentenceTransformer


_MODEL = None


def get_embedding_model() -> SentenceTransformer:
    global _MODEL

    if _MODEL is None:
        _MODEL = SentenceTransformer(
            "sentence-transformers/all-MiniLM-L6-v2"
        )

    return _MODEL

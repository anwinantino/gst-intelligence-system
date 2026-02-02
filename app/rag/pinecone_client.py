from pinecone import Pinecone
from app.core.config import settings


def get_pinecone_index():
    pc = Pinecone(api_key=settings.pinecone_api_key)
    return pc.Index(settings.pinecone_index_name)

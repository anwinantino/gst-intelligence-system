from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

from app.core.config import settings


DATABASE_URL = (
    f"mysql+mysqlconnector://{settings.mysql_user}:"
    f"{settings.mysql_password}@{settings.mysql_host}:"
    f"{settings.mysql_port}/{settings.mysql_db}"
)

engine = create_engine(
    DATABASE_URL,
    pool_pre_ping=True,
    echo=False,
)

SessionLocal = sessionmaker(
    bind=engine,
    autocommit=False,
    autoflush=False,
)
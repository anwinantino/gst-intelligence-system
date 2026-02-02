from pydantic_settings import BaseSettings
from pydantic import ConfigDict


class Settings(BaseSettings):
    mysql_host: str
    mysql_port: int
    mysql_user: str
    mysql_password: str
    mysql_db: str

    model_config = ConfigDict(
        env_file=".env",
        extra="ignore",   # 👈 THIS LINE FIXES THE ERROR
    )


settings = Settings()

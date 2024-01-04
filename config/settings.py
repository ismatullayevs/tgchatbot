import os
from dotenv import load_dotenv

load_dotenv()

# TODO: use pydantic
class Settings:
    BOT_TOKEN: str = os.getenv("BOT_TOKEN") or ''
    OPENAI_API_KEY: str = os.getenv("OPENAI_API_KEY") or ''
    DATABASE_URL: str = os.getenv("DATABASE_URL") or ''


settings = Settings()

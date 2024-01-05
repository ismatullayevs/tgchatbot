import os
from dotenv import load_dotenv

load_dotenv()


class Settings:
    SECRET_KEY: str = os.getenv("SECRET_KEY") or 'changethis'
    DEBUG: bool = os.getenv("DEBUG") == 'True'

    BOT_TOKEN: str = os.getenv("BOT_TOKEN") or ''
    OPENAI_API_KEY: str = os.getenv("OPENAI_API_KEY") or ''

    DB_NAME: str = os.getenv("POSTGRES_DB") or ''
    DB_USER: str = os.getenv("POSTGRES_USER") or ''
    DB_PASSWORD: str = os.getenv("POSTGRES_PASSWORD") or ''
    DB_HOST: str = os.getenv("POSTGRES_HOST") or ''
    DB_PORT = int(os.getenv("POSTGRES_PORT") or '')

    DATABASE_URL: str = f"postgres://{DB_USER}:{
        DB_PASSWORD}@{DB_HOST}:{DB_PORT}/{DB_NAME}"

    DB_CONFIG = {
        'connections': {
            'default': DATABASE_URL
        },
        'apps': {
            'models': {
                'models': ['app.models.user', 'app.models.message'],
                'default_connection': 'default',
            }
        }
    }


settings = Settings()

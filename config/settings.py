from dotenv import load_dotenv
from .utils import get_env, boolean


load_dotenv()


class Settings:
    SECRET_KEY = get_env("SECRET_KEY")
    DEBUG = get_env("DEBUG", cast=boolean)

    BOT_TOKEN = get_env("BOT_TOKEN")
    OPENAI_API_KEY = get_env("OPENAI_API_KEY")

    DB_NAME = get_env("POSTGRES_DB")
    DB_USER = get_env("POSTGRES_USER")
    DB_PASSWORD = get_env("POSTGRES_PASSWORD")
    DB_HOST = get_env("POSTGRES_HOST")
    DB_PORT = get_env("POSTGRES_PORT", cast=int)

    DATABASE_URL = f"postgres://{DB_USER}:{
        DB_PASSWORD}@{DB_HOST}:{DB_PORT}/{DB_NAME}"
    # DATABASE_URL = 'sqlite://db.sqlite3'

    DB_CONFIG = {
        'connections': {
            'default': DATABASE_URL
        },
        'apps': {
            'models': {
                'models': ['app.models.user', 'app.models.message', 'aerich.models'],
                'default_connection': 'default',
            }
        }
    }

    # ChatGPT settings
    MAX_HISTORY: int | None = 20
    SYSTEM_MESSAGE: str | None = None


settings = Settings()

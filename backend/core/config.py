import os
from pathlib import Path
from pydantic_settings import BaseSettings
from dotenv import load_dotenv


env_path = Path(__file__).resolve().parent.parent / ".env"

print(f"Looking for .env file at: {env_path}")


load_dotenv(dotenv_path=env_path)

class Settings(BaseSettings):
    PROJECT_NAME: str = "Gemini Adventure"
    API_PREFIX: str = "/api"
    DEBUG: bool = True

 
    DATABASE_URL: str
    GOOGLE_API_KEY: str

    class Config:
        case_sensitive = True


try:
    settings = Settings()
    print(f" Configuration loaded successfully!")
except Exception as e:
    print(f" Failed to load settings. Ensure .env exists at the path above.")
    raise e
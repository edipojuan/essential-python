from dotenv import load_dotenv
import os

load_dotenv()

class Config:
    DATABASE_URL: str = os.getenv("DATABASE_URL", "postgresql://postgres:postgres@localhost:5432/langfuse")
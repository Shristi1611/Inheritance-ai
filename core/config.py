import os
from dotenv import load_dotenv

load_dotenv()

class Config:
    GROQ_API_KEY: str = os.getenv("GROQ_API_KEY", "")
    LLM_MODEL: str = "llama-3.3-70b-versatile"
    WHISPER_MODEL: str = "whisper-large-v3"
    OWNER_NAME: str = os.getenv("OWNER_NAME", "the author")
    DATASET: str = "inheritance_memory"
config = Config()
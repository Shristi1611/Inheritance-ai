from groq import Groq
from core.config import config

client = Groq(api_key=config.GROQ_API_KEY)

async def transcribe_audio(file_path: str) -> str:
    with open(file_path, "rb") as audio_file:
        transcription = client.audio.transcriptions.create(
            model=config.WHISPER_MODEL,
            file=audio_file,
            response_format="text"
        )
    print(f"[transcribe] done: {file_path}")
    return transcription
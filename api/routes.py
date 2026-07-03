from fastapi import APIRouter, UploadFile, File, Form
from fastapi.responses import JSONResponse
from core.memory import remember, recall, improve, forget
from core.transcribe import transcribe_audio
from core.config import config
import aiofiles
import os

router = APIRouter()

@router.post("/remember/text")
async def remember_text(text: str = Form(...), source: str = Form(default="manual")):
    await remember(text, source_label=source)
    return {"status": "remembered", "source": source}

@router.post("/remember/file")
async def remember_file(file: UploadFile = File(...)):
    content = await file.read()
    text = content.decode("utf-8")
    await remember(text, source_label=file.filename)
    return {"status": "remembered", "file": file.filename}

@router.post("/remember/voice")
async def remember_voice(file: UploadFile = File(...)):
    save_path = os.path.join(config.DATA_VOICES_DIR, file.filename)
    async with aiofiles.open(save_path, "wb") as f:
        await f.write(await file.read())
    text = await transcribe_audio(save_path)
    await remember(text, source_label=f"voice:{file.filename}")
    return {"status": "remembered", "transcript": text}

@router.post("/recall")
async def recall_memory(query: str = Form(...)):
    answer = await recall(query)
    return {"answer": answer}

@router.post("/improve")
async def improve_memory():
    await improve()
    return {"status": "memory enriched"}

@router.post("/forget")
async def forget_memory():
    await forget()
    return {"status": "memory cleared"}
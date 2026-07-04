from dotenv import load_dotenv
load_dotenv()

from fastapi import FastAPI
from fastapi.staticfiles import StaticFiles
from fastapi.responses import FileResponse
from contextlib import asynccontextmanager
from core.memory import setup_cognee
from api.routes import router

from core.demo_data import load_demo_data

@asynccontextmanager
async def lifespan(app: FastAPI):
    await setup_cognee()
    await load_demo_data()
    print("[startup] Cognee is ready")
    yield

app = FastAPI(
    title="The Inheritance",
    description="A queryable memory you build for someone else.",
    lifespan=lifespan
)

app.include_router(router)
app.mount("/static", StaticFiles(directory="static"), name="static")

@app.get("/")
async def serve_ui():
    return FileResponse("static/index.html")
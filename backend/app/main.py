from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from backend.app.routes import summarize, audio

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(summarize.router)
app.include_router(audio.router)


@app.get("/")
def home():
    return {
        "message": "Lecture-to-Notes API running"
    }

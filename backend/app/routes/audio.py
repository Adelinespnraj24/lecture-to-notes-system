from fastapi import APIRouter, UploadFile, File
import shutil
import os

from backend.app.services.speech_to_text import transcribe_audio
from backend.app.services.summarizer import get_summary
from backend.app.services.sentiment import analyze_sentiment
from backend.app.services.history import save_history

router = APIRouter()

UPLOAD_DIR = "temp_audio"
os.makedirs(UPLOAD_DIR, exist_ok=True)


@router.post("/audio-to-notes")
async def audio_to_notes(
    file: UploadFile = File(...),
    mode: str = "Short"
):

    file_path = f"{UPLOAD_DIR}/{file.filename}"

    with open(file_path, "wb") as buffer:
        shutil.copyfileobj(file.file, buffer)

    transcript = transcribe_audio(file_path)

    summary = get_summary(
        transcript,
        mode
    )

    sentiment = analyze_sentiment(
        transcript
    )

    save_history({
        "input": transcript,
        "summary": summary,
        "sentiment": sentiment
    })

    return {
        "transcript": transcript,
        "summary": summary,
        "sentiment": sentiment
    }

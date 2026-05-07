from fastapi import APIRouter
from pydantic import BaseModel

from backend.app.services.summarizer import get_summary
from backend.app.services.sentiment import analyze_sentiment
from backend.app.services.history import save_history

router = APIRouter()


class TextRequest(BaseModel):
    text: str
    mode: str = "Short"


@router.post("/summarize")
def summarize_text(request: TextRequest):

    summary = get_summary(
        request.text,
        request.mode
    )

    sentiment = analyze_sentiment(
        request.text
    )

    save_history({
        "input": request.text,
        "summary": summary,
        "sentiment": sentiment
    })

    return {
        "summary": summary,
        "sentiment": sentiment
    }

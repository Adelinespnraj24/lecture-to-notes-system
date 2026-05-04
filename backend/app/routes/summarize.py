from fastapi import APIRouter
from pydantic import BaseModel
from backend.app.services.summarizer import get_summary

router = APIRouter()

class TextRequest(BaseModel):
    text: str

@router.post("/summarize")
def summarize_text(request: TextRequest):
    summary = get_summary(request.text)
    return {"summary": summary}
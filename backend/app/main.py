from fastapi import FastAPI
from backend.app.routes import summarize

app = FastAPI()

app.include_router(summarize.router)

@app.get("/")
def home():
    return {"message": "Lecture-to-Notes API running"}
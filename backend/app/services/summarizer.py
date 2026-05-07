from transformers import pipeline
import re

summarizer = pipeline(
    "summarization",
    model="facebook/bart-large-cnn"
)


def clean_text(text):
    text = text.strip()
    text = re.sub(r'\s+', ' ', text)
    return text


def get_summary(text, mode="Short"):

    text = clean_text(text)

    word_count = len(text.split())

    if word_count < 50:
        return text

    if mode == "Short":
        max_len = 60
        min_len = 20

    elif mode == "Detailed":
        max_len = 120
        min_len = 50

    elif mode == "Bullet Points":
        max_len = 100
        min_len = 40

    else:
        max_len = 80
        min_len = 30

    result = summarizer(
        text,
        max_length=max_len,
        min_length=min_len,
        do_sample=False
    )

    summary = result[0]["summary_text"]

    if mode == "Bullet Points":
        sentences = summary.split('. ')
        bullets = "\n".join([f"• {s}" for s in sentences if s])
        return bullets

    return summary

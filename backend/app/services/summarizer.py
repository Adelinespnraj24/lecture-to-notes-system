from transformers import pipeline

summarizer = pipeline(
    "summarization",
    model="sshleifer/distilbart-cnn-12-6"
)

def get_summary(text):
    result = summarizer(
        text,
        max_length=120,
        min_length=50,
        do_sample=False
    )
    return result[0]['summary_text']
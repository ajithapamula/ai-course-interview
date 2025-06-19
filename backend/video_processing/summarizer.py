from transformers import pipeline

# Load the summarization model
summarizer = pipeline("summarization", model="sshleifer/distilbart-cnn-12-6")

def generate_summary(text: str) -> str:
    if not text.strip():
        return ""
    result = summarizer(text, max_length=100, min_length=30, do_sample=False)
    return result[0]['summary_text']

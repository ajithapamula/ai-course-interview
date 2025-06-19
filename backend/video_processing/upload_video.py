import os
from datetime import datetime
from faster_whisper import WhisperModel
from fastapi import UploadFile
from backend.video_processing.db import save_to_mongodb
from backend.video_processing.summarizer import generate_summary

UPLOAD_DIR = "uploads"
os.makedirs(UPLOAD_DIR, exist_ok=True)

model = WhisperModel("base")

async def save_and_transcribe(file: UploadFile):
    # Save to uploads folder
    file_path = os.path.join(UPLOAD_DIR, file.filename)
    with open(file_path, "wb") as buffer:
        buffer.write(await file.read())

    # Transcribe
    segments, info = model.transcribe(file_path)
    transcript = " ".join([segment.text for segment in segments])

    # Generate summary
    summary = generate_summary(transcript)

    # Store in MongoDB
    data = {
        "filename": file.filename,
        "filepath": file_path,
        "transcript": transcript,
        "summary": summary,
        "duration": info.duration,
        "language": info.language,
        "timestamp": datetime.utcnow()
    }
    save_to_mongodb(data)

    return {
        "transcript": transcript,
        "summary": summary,
        "duration": info.duration,
        "language": info.language
    }

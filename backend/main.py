from fastapi import FastAPI, File, UploadFile
from fastapi.middleware.cors import CORSMiddleware
from backend.video_processing.upload_video import save_and_transcribe

app = FastAPI()

# Allow frontend to connect
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # Set frontend URL later
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.get("/")
def root():
    return {"message": "AI Interview Coach API is running."}

@app.post("/upload/")
async def upload_video(file: UploadFile = File(...)):
    result = await save_and_transcribe(file)
    return result

# 🎥 AI Course Interview Processing Platform

## 🌟 Introduction

**AI Course Interview** is a full-stack AI-powered application that helps you process course or interview recordings.  

Upload a video from your local device or app, and the system will automatically:  

1. 🎬 **Compress the video** to save space  
2. 🔇 Apply **noise cancellation** for better clarity  
3. 📝 Generate a **full transcript** using speech-to-text  
4. 📑 Create a **summary** of the key points  
5. 📂 Export the summary as a **PDF**  
6. 🗄️ Store everything (**video, audio, transcript, PDF, metadata**) in **MongoDB**  

This makes it perfect for **online course recordings, interviews, and meeting archives**.

---

## ⚡ Features

- 📤 **Upload video** from local storage or other apps  
- 🔄 **Automatic processing pipeline** (compression → cleaning → transcription → summary → PDF)  
- 🗂️ **MongoDB storage** for all files & metadata  
- 🔍 **Easy retrieval** via frontend or API  
- 🚀 Ready for scaling with Docker & cloud deployment  

---

🛠️ Tech Stack

Frontend: React / Next.js (video upload, results display)
Backend: Python (FastAPI / Flask)
Processing Tools: FFmpeg, Speech-to-Text (Whisper / HuggingFace), Transformers for summarization
Database: MongoDB
Reports: ReportLab / FPDF for PDF generation

ai-course-interview/
├── backend/               # Backend (APIs, video/audio processing logic)
│   ├── main.py            # Entry point for FastAPI/Flask server
│   ├── utils/             # Helper functions (compression, noise cancellation, transcription)
│   └── ...
├── frontend/              # React / Next.js frontend (upload & display)
├── requirements.txt       # Python dependencies
├── package.json           # Frontend dependencies (if React used)
├── docker-compose.yml     # Dockerized setup
├── README.md              # Documentation (this file)
└── ...

🚀 Getting Started
1️⃣ Clone the repository
git clone https://github.com/ajithapamula/ai-course-interview.git
cd ai-course-interview

2️⃣ Setup Backend (Python)
cd backend
python3 -m venv venv
source venv/bin/activate
pip install -r requirements.txt


Create a .env file inside backend/:

MONGO_URI=mongodb://localhost:27017
MONGO_DB=ai_course_db

uvicorn main:app --reload

3️⃣ Setup Frontend (React/Next.js)
cd frontend
npm install
npm run dev


Frontend will now run at 👉 http://localhost:3000


---

👉 This version now has a **clear beginning → setup → usage → workflow → ending notes** flow.  


## 🏗️ Project Architecture

```mermaid
flowchart TD
    A[📤 User Uploads Video] --> B[🎬 Video Compression]
    B --> C[🔇 Noise Cancellation]
    C --> D[📝 Speech-to-Text Transcription]
    D --> E[📑 Summary + PDF Export]
    E --> F[🗄️ Store in MongoDB]
    F --> G[📤 Retrieve Transcript / PDF / Video]

from fastapi import FastAPI, UploadFile, File
from fastapi.responses import FileResponse
import shutil
import uuid
import os

app = FastAPI()

UPLOAD_DIR = "uploads"

if not os.path.exists(UPLOAD_DIR):
    os.makedirs(UPLOAD_DIR)


@app.get("/")
def home():
    return {"status": "SmokeWatch AI backend running"}


@app.post("/upload")
async def upload_video(file: UploadFile = File(...)):

    video_id = str(uuid.uuid4())
    file_path = f"{UPLOAD_DIR}/{video_id}.mp4"

    with open(file_path, "wb") as buffer:
        shutil.copyfileobj(file.file, buffer)

    return {
        "video_id": video_id,
        "video_url": f"/video/{video_id}"
    }


@app.get("/video/{video_id}")
def get_video(video_id: str):

    file_path = f"{UPLOAD_DIR}/{video_id}.mp4"

    return FileResponse(file_path)


@app.post("/process/{video_id}")
def process_video(video_id: str):

    # simulated AI detection (real YOLO comes next)

    return {
        "video_id": video_id,
        "smoking_detected": True,
        "confidence": 0.93,
        "events": [
            {"start": "00:12", "end": "00:17", "confidence": 0.91},
            {"start": "01:02", "end": "01:08", "confidence": 0.95}
        ]
    }

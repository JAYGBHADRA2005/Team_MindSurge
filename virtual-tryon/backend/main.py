from fastapi import FastAPI, File, UploadFile, HTTPException, Form
from fastapi.middleware.cors import CORSMiddleware
from fastapi.staticfiles import StaticFiles
from pydantic import BaseModel
import os
import shutil
import uuid

app = FastAPI(title="Virtual Try-On API")

# Allow widget to call API from e-commerce sites
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # replace with specific domains in production
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

UPLOAD_DIR = "uploads"
VIDEO_DIR = "videos"
os.makedirs(UPLOAD_DIR, exist_ok=True)
os.makedirs(VIDEO_DIR, exist_ok=True)

class TryOnResponse(BaseModel):
    video_url: str

@app.post("/api/try-on", response_model=TryOnResponse)
async def try_on(product_id: str = Form(...), file: UploadFile = File(...)):
    """Receive selfie and product info, call AI API, and return video URL."""
    # Save selfie locally
    selfie_id = str(uuid.uuid4())
    selfie_path = os.path.join(UPLOAD_DIR, f"{selfie_id}_{file.filename}")
    with open(selfie_path, "wb") as buffer:
        shutil.copyfileobj(file.file, buffer)

    try:
        # TODO: Replace with call to external AI service (HeyGen/RunwayML)
        # For demonstration, copy a sample video to simulate processing
        sample_video = os.path.join("static", "sample.mp4")
        generated_video = os.path.join(VIDEO_DIR, f"{selfie_id}.mp4")
        shutil.copyfile(sample_video, generated_video)
    except Exception as e:
        raise HTTPException(status_code=500, detail="AI processing failed")

    return {"video_url": f"/videos/{selfie_id}.mp4"}

app.mount("/videos", StaticFiles(directory=VIDEO_DIR), name="videos")
app.mount("/static", StaticFiles(directory="static"), name="static")

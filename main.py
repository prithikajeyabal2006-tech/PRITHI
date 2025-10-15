from fastapi import FastAPI, File, UploadFile, Form
from fastapi.middleware.cors import CORSMiddleware
from app.speech import transcribe_audio
from app.nlp import analyze_text
from app.database import save_result, init_db
from tempfile import NamedTemporaryFile
import shutil

app = FastAPI()
app.add_middleware(CORSMiddleware, allow_origins=["*"], allow_methods=["*"], allow_headers=["*"])

@app.on_event("startup")
def startup():
    init_db()

@app.post("/analyze")
async def analyze(audio: UploadFile = File(...), candidate_name: str = Form(None)):
    # save uploaded file to temp
    with NamedTemporaryFile(delete=False, suffix=".wav") as tmp:
        shutil.copyfileobj(audio.file, tmp)
        tmp_path = tmp.name

    transcript = transcribe_audio(tmp_path)
    metrics = analyze_text(transcript)
    result = {
        "candidate_name": candidate_name,
        "transcript": transcript,
        **metrics
    }
    save_result(result)
    return result

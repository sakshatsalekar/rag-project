from fastapi import FastAPI, UploadFile, File
import shutil
from rag import read_pdf, process_text, search_text

app = FastAPI()

@app.get("/")
def home():
    return {"message": "API is running"}

@app.post("/upload")
def upload(file: UploadFile = File(...)):
    file_path = file.filename

    with open(file_path, "wb") as buffer:
        shutil.copyfileobj(file.file, buffer)

    text = read_pdf(file_path)

    process_text(text)

    return {"message": "File uploaded and processed with AI"}

@app.get("/search")
def search(query: str):
    results = search_text(query)
    return {"results": results}
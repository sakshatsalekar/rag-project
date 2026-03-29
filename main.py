from fastapi import FastAPI, UploadFile, File, Depends, HTTPException
from fastapi.security import HTTPBearer, HTTPAuthorizationCredentials
import shutil

from rag import read_pdf, process_text, search_text
from auth import create_token, verify_token

app = FastAPI()

# 🔐 Security
security = HTTPBearer()

def get_current_user(credentials: HTTPAuthorizationCredentials = Depends(security)):
    token = credentials.credentials
    print("TOKEN:", token)

    payload = verify_token(token)
    print("PAYLOAD:", payload)

    if payload is None:
        raise HTTPException(status_code=401, detail="Invalid or expired token")

    return payload

# 🧑 Dummy user (for demo)
fake_user = {
    "username": "admin",
    "password": "1234",
    "role": "admin"
}

# 🔐 Auth APIs
@app.post("/auth/login")
def login(username: str, password: str):
    if username != fake_user["username"] or password != fake_user["password"]:
        return {"error": "Invalid credentials"}

    token = create_token({"sub": username, "role": "admin"})
    return {"access_token": token}

# 🏠 Home
@app.get("/")
def home():
    return {"message": "API is running"}

# 📄 Upload PDF
@app.post("/upload")
def upload(
    file: UploadFile = File(...),
    user = Depends(get_current_user)
):
    file_path = file.filename

    with open(file_path, "wb") as buffer:
        shutil.copyfileobj(file.file, buffer)

    text = read_pdf(file_path)
    process_text(text)

    return {"message": "File uploaded and processed"}

# 🔍 Search
@app.get("/search")
def search(
    query: str,
    user = Depends(get_current_user)
):
    if not query:
        return {"error": "Query cannot be empty"}

    results = search_text(query)
    return {"results": results}
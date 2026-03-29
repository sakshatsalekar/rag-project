# RAG Document Search API

## Features
- Upload PDF documents
- Extract text using pdfplumber
- Semantic search using SentenceTransformers
- Vector search using FAISS

## Tech Stack
- FastAPI
- SentenceTransformers
- FAISS
- Python

## How to Run

```bash
pip install -r requirements.txt
uvicorn main:app --reload
import pdfplumber
from sentence_transformers import SentenceTransformer
import faiss
import numpy as np

model = SentenceTransformer("all-MiniLM-L6-v2")

index = faiss.IndexFlatL2(384)
stored_chunks = []

def read_pdf(file):
    text = ""
    with pdfplumber.open(file) as pdf:
        for page in pdf.pages:
            text += page.extract_text() or ""
    return text

def chunk_text(text):
    return [text[i:i+500] for i in range(0, len(text), 500)]

def process_text(text):
    chunks = chunk_text(text)
    embeddings = model.encode(chunks)

    index.add(np.array(embeddings))
    stored_chunks.extend(chunks)

def search_text(query):
    query_embedding = model.encode([query])
    D, I = index.search(query_embedding, k=3)

    return [stored_chunks[i] for i in I[0]]
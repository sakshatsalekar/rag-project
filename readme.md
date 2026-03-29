# 🚀 RAG-Based Document Search System

## 📌 Overview
This project is an AI-powered document search system built using FastAPI and semantic search techniques. It allows users to upload PDF documents, process them into embeddings, and perform intelligent search using natural language queries.

---

## 🔥 Features
- 📄 Upload and process PDF documents
- 🧠 Semantic search using embeddings
- ⚡ Fast retrieval using FAISS
- 🔐 JWT Authentication for secure APIs
- 🚀 FastAPI backend

---

## 🛠 Tech Stack
- Python
- FastAPI
- Sentence Transformers
- FAISS
- JWT Authentication

---

## 📂 Project Structure


---

## 🚀 How to Run

```bash
pip install -r requirements.txt
uvicorn main:app --reload

Open:

http://127.0.0.1:8000/docs

🔐 Authentication
Call /auth/login
Copy token
Click Authorize
Use: Bearer YOUR_TOKEN

Example Query
What is the role of admin?


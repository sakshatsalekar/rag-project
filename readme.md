## How to Run

### Step 1: Clone Repo
git clone https://github.com/sakshatsalekar/rag-project

### Step 2: Go to folder
cd rag-project

### Step 3: Install dependencies
pip install -r requirements.txt

### Step 4: Run server
uvicorn main:app --reload

### Step 5: Open in browser
http://127.0.0.1:8000/docs

## Example Usage

1. Upload a PDF using `/upload`
2. Search using `/search?query=your_query`
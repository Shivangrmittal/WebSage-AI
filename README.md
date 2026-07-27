# 🌐 WebSage

> **An AI-powered Chrome Extension that lets you chat with any webpage using Retrieval-Augmented Generation (RAG).**

WebSage is an intelligent Chrome extension that understands the content of the webpage you are currently viewing and answers your questions using AI. It extracts webpage content, creates embeddings, stores them in a FAISS vector database, retrieves the most relevant information, and generates accurate, context-aware responses using a Large Language Model.

---

## ✨ Features

- 🌐 Chat with any webpage
- 🧠 Retrieval-Augmented Generation (RAG)
- 📄 Automatic webpage content extraction
- ✂️ Intelligent document chunking
- 🔍 Semantic search with FAISS
- 🤖 AI-powered responses using Qwen 2.5
- 💬 Conversation memory
- ⚡ FastAPI backend
- 🧩 Chrome Extension (Manifest V3)
- 🎨 Clean and responsive user interface
- 🚀 Fast and lightweight

---

## 🏗️ Architecture

```text
                    Chrome Extension
                           │
                           ▼
                  FastAPI Backend
                           │
         ┌─────────────────┴─────────────────┐
         ▼                                   ▼
  Webpage Loader                    Conversation Memory
         │
         ▼
 Document Splitter
         │
         ▼
 HuggingFace Embeddings
         │
         ▼
     FAISS Vector Store
         │
         ▼
 Similarity Search
         │
         ▼
      Qwen 2.5 LLM
         │
         ▼
      AI Response
```

---

## 🛠️ Tech Stack

### Frontend

- Chrome Extension (Manifest V3)
- HTML
- CSS
- JavaScript

### Backend

- FastAPI
- LangChain
- Hugging Face Inference API
- FAISS
- Trafilatura
- Python

### AI & NLP

- Qwen 2.5-72B-Instruct
- HuggingFace Embeddings
- Recursive Character Text Splitter
- Retrieval-Augmented Generation (RAG)

---


## 🚀 Installation

### 1. Clone the Repository

```bash
git clone https://github.com/Shivangrmittal/WebSage-AI.git

cd WebSage
```

---

### 2. Create a Virtual Environment

```bash
cd backend

python -m venv venv
```

Activate it

**Windows**

```bash
venv\Scripts\activate
```

**Linux / macOS**

```bash
source venv/bin/activate
```

---

### 3. Install Dependencies

```bash
pip install -r requirements.txt
```

---

### 4. Configure Environment Variables

Create a `.env` file inside the `backend` folder.

```env
HUGGINGFACEHUB_API_TOKEN=your_huggingface_api_token
```

---

### 5. Start the Backend

```bash
uvicorn app:app --reload
```

The backend will start at

```
http://127.0.0.1:8000
```

---

### 6. Load the Chrome Extension

1. Open Chrome.
2. Go to `chrome://extensions/`
3. Enable **Developer Mode**.
4. Click **Load unpacked**.
5. Select the `extension` folder.

The extension is now ready to use.

---

## 💡 How It Works

1. Open any webpage.
2. Click the WebSage extension.
3. Ask a question about the webpage.
4. The backend extracts the webpage content.
5. The content is split into smaller chunks.
6. Embeddings are generated using HuggingFace.
7. Chunks are stored in a FAISS vector database.
8. Relevant chunks are retrieved using semantic similarity.
9. The retrieved context and user query are sent to the Qwen 2.5 language model.
10. The generated answer is displayed inside the extension.

---


## 👨‍💻 Author

**Shivang Raj Mittal**

GitHub: https://github.com/Shivangrmittal

LinkedIn: https://www.linkedin.com/in/shivang-raj-mittal-8986b1298/

from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel
from embeddings import get_embedding_model
from loaders import load_webpage
from splitter import split_documents
from vectorstore import create_vector_store
from rag import process_query

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


class ChatRequest(BaseModel):
    question: str
    url: str


@app.get("/")
def home():
    return {
        "message": "Backend Running"
    }


@app.post("/chat")
def chat(request: ChatRequest):

    result = process_query(
        request.url,
        request.question
    )

    return {

        "answer": result["answer"]

    }
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel
from transformers import pipeline

# Create FastAPI app
app = FastAPI(
    title="AI-Assisted Text Classification API",
    description="Text classification using BERT + rule-based logic",
    version="1.0"
)

# Enable CORS (optional for frontend development)
origins = ["*"]  # Allow all origins for dev
app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_methods=["*"],
    allow_headers=["*"]
)

# Load BERT sentiment model
classifier = pipeline(
    "sentiment-analysis",
    model="distilbert-base-uncased-finetuned-sst-2-english"
)

# Request body schema
class TextInput(BaseModel):
    text: str

# Health check
@app.get("/")
def health():
    return {"status": "BERT microservice running"}

# Classification endpoint
@app.post("/classify")
def classify_text(input: TextInput):
    text = input.text.lower().strip()

    # Rule-based Query detection
    query_keywords = [
        "how", "what", "when", "where", "why",
        "can", "could", "do i", "does", "is it"
    ]

    if "?" in text or any(text.startswith(q) for q in query_keywords):
        return {
            "category": "Query",
            "confidence": 0.9
        }

    # Sentiment-based classification using BERT
    result = classifier(input.text)[0]
    label = result["label"]
    score = result["score"]

    if label == "NEGATIVE":
        category = "Complaint"
    else:
        category = "Feedback"

    return {
        "category": category,
        "confidence": round(score, 2)
    }

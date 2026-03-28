# app/api/routes/chat.py
from fastapi import APIRouter
from app.schemas.chat import ChatRequest, ChatResponse
from app.services.classifier import classify_message
from app.services.sentiment import sentiment_score
from app.services.llm import generate_response
from app.core.security import validate_email

router = APIRouter()

@router.post("/chat", response_model=ChatResponse)
def chat(req: ChatRequest):

    validate_email(req.email)

    msg_type = classify_message(req.message)
    sentiment = sentiment_score(req.message)

    # NOT calling LLM for all cases
    if msg_type == "number":
        return {
            "type": msg_type,
            "sentiment": "neutral",
            "response": f"Number received: {req.message}"
        }

    if msg_type == "deadline":
        return {
            "type": msg_type,
            "sentiment": "neutral",
            "response": "Deadline noted."
        }

    # Only for tone
    response = generate_response(req.message)

    return {
        "type": msg_type,
        "sentiment": sentiment,
        "response": response
    }
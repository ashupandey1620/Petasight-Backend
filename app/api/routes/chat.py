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
    response = generate_response(req.message)

    return {
        "type": msg_type,
        "sentiment": sentiment,
        "response": response
    }
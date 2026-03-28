# app/schemas/chat.py
from pydantic import BaseModel, EmailStr

class ChatRequest(BaseModel):
    message: str
    email: EmailStr

class ChatResponse(BaseModel):
    type: str
    sentiment: str
    response: str
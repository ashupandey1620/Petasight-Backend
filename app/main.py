# app/main.py
from fastapi import FastAPI
from app.api.routes.chat import router

app = FastAPI(title="AI Chatbot API")

app.include_router(router, prefix="/api")
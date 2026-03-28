# app/services/classifier.py
import re

def classify_message(msg: str):
    msg = msg.strip().lower()

    if re.search(r"\b(\d+)\s*(hours|hrs|minutes|min|hour|minute|second|seconds|sec)\b", msg):
        return "deadline"

    if re.fullmatch(r"\d+", msg):
        return "number"

    return "tone"
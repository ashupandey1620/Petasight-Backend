# app/services/llm.py
from openai import OpenAI
from app.core.config import settings

# client = OpenAI(api_key=settings.OPENAI_API_KEY)

from openai import OpenAI

client = OpenAI(
    api_key=settings.OPENAI_API_KEY,
    base_url="https://api.groq.com/openai/v1"
)


SYSTEM_PROMPT = """
You are a political leader.
Respond in Hindi.
Also provide English translation.

Tone should match user sentiment.
"""

def generate_response(user_msg: str):
    response = client.chat.completions.create(
        model="llama-3.3-70b-versatile",
        temperature=0.7,
        messages=[
            {"role": "system", "content": SYSTEM_PROMPT},
            {"role": "user", "content": user_msg}
        ]
    )
    return response.choices[0].message.content
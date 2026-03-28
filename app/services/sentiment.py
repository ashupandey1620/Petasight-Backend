# app/services/sentiment.py

def sentiment_score(msg: str):
    msg = msg.lower()

    score = 0
    positive = ["happy", "great", "awesome", "love"]
    negative = ["sad", "bad", "angry", "depressed"]

    for w in positive:
        if w in msg:
            score += 1

    for w in negative:
        if w in msg:
            score -= 1

    if score <= -2:
        return "very_sad"
    elif score < 0:
        return "sad"
    elif score == 0:
        return "neutral"
    elif score == 1:
        return "happy"
    return "very_happy"
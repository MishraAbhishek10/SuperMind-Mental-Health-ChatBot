def detect_mood(text: str) -> str:
    text = text.lower()

    stressed = ["stress", "pressure", "overwhelmed", "burnout", "tired"]
    anxious = ["anxious", "worried", "panic", "nervous", "fear"]
    sad = ["sad", "lonely", "down", "depressed", "upset"]
    happy = ["happy", "good", "great", "fine", "excited"]

    if any(w in text for w in stressed):
        return "Stressed"
    if any(w in text for w in anxious):
        return "Anxious"
    if any(w in text for w in sad):
        return "Sad"
    if any(w in text for w in happy):
        return "Happy"

    return "Neutral"
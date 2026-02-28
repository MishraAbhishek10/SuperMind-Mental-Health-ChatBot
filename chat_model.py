from dotenv import load_dotenv
import os
from groq import Groq

load_dotenv()

API_KEY = os.getenv("GROQ_API_KEY")

if not API_KEY:
    raise ValueError("GROQ_API_KEY not found in .env")

client = Groq(api_key=API_KEY)

# SYSTEM_PROMPT = """
# You are a kind, supportive mental health companion.
# You must:
# - Be empathetic
# - Be calm and friendly
# - Never give medical advice
# - Keep responses under 120 words
#"""


def get_chat_response(message: str, mood: str):

    SYSTEM_PROMPT = f"""
        You are a calm, supportive mental health companion.

        User mood: {mood}
        User message: {message}

        Rules for your response:
        - Be empathetic but concise
        - Do NOT sound like a long essay
        - Use simple, friendly language
        - Avoid repeating the same advice every time
        - Do NOT give medical or clinical advice
        - Keep the response under 90 words
        STRICT RULES (MUST FOLLOW):
        - Be empathetic but concise
        - Do NOT give medical advice
        - Response MUST be under 90 words
        - Use Markdown formatting ONLY
        - Do NOT put multiple bullet points on the same line

        Response structure:
        1️⃣ One short empathetic sentence (1 line max)
        2️⃣ 3–4 calming suggestions as bullet points
        3️⃣ End with ONE gentle follow-up question

        Example style:
        "I’m really glad you shared this with me 💙  
        Here are a few gentle things you could try:
        • item1
        • item2
        • item3
        What feels easiest for you right now?"

        Now respond.
        """
    completion = client.chat.completions.create(
        # model="llama3-70b-8192",
        model="llama-3.1-8b-instant",
        messages=[
            {"role": "system", "content": SYSTEM_PROMPT},
            {"role": "user", "content": f"My mood is {mood}. {message}"}
        ]
    )

    return completion.choices[0].message.content


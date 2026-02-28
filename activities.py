def get_activities(mood: str):
    suggestions = {
        "Stressed": [
            "🧘 Do 5 deep breaths",
            "🚶 Take a 5-minute walk",
            "💧 Drink a glass of water"
        ],
        "Anxious": [
            "📝 Write what you’re worried about",
            "🌬️ Try slow breathing",
            "🎧 Listen to calm music"
        ],
        "Sad": [
            "📞 Message someone you trust",
            "🌤️ Step outside for fresh air",
            "📖 Read something light"
        ],
        "Happy": [
            "🎨 Do something creative",
            "🤝 Help someone",
            "🗓️ Plan something fun"
        ],
        "Neutral": [
            "📂 Organize one small thing",
            "☕ Take a short break",
            "🚶 Stretch your body"
        ]
    }

    return suggestions.get(mood, suggestions["Neutral"])
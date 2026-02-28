# import speech_recognition as sr

# def get_voice_input():
#     r = sr.Recognizer()
#     with sr.Microphone() as source:
#         r.adjust_for_ambient_noise(source)
#         audio = r.listen(source)

#     try:
#         text = r.recognize_google(audio)
#         return text
#     except:
#         return None
    

import speech_recognition as sr
import tempfile
import os

def speech_to_text(audio_bytes):
    recognizer = sr.Recognizer()

    try:
        # Save audio bytes to temp WAV file
        with tempfile.NamedTemporaryFile(delete=False, suffix=".wav") as temp_audio:
            temp_audio.write(audio_bytes)
            temp_audio_path = temp_audio.name

        # Convert speech to text
        with sr.AudioFile(temp_audio_path) as source:
            audio = recognizer.record(source)
            text = recognizer.recognize_google(audio)

        os.remove(temp_audio_path)
        return text

    except Exception as e:
        print("Speech error:", e)
        return None
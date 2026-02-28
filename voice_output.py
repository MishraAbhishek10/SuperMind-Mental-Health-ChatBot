
import pyttsx3
import threading

engine = pyttsx3.init()
engine.setProperty("rate", 160)

def speak(text):
    def run_tts():
        engine.say(text)
        engine.runAndWait()

    t = threading.Thread(target=run_tts)
    t.start()


# import pyttsx3
# import threading

# engine = pyttsx3.init()
# engine.setProperty("rate", 160)

# def speak(text):
#     pass
#     def run_tts():
#         engine.say(text)
#         engine.runAndWait()

#     t = threading.Thread(target=run_tts)
#     t.start()
import os

IS_CLOUD = True   # set False locally

if IS_CLOUD:
    def speak(text):
        pass
else:
    import pyttsx3
    engine = pyttsx3.init()
    engine.setProperty("rate", 160)

    def speak(text):
        engine.say(text)
        engine.runAndWait()





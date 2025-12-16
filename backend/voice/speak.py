import pyttsx3
from backend.core.state import set_state

engine = pyttsx3.init()
engine.setProperty("rate", 165)

def speak(text: str):
    if not text:
        return

    try:
        set_state("speaking")
        print("🗣️ CRONOS dice:", text)
        engine.say(text)
        engine.runAndWait()
    finally:
        set_state("idle")

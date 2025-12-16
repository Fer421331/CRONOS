import pyttsx3
import requests

API_URL = "http://localhost:8000/state"

engine = pyttsx3.init()
engine.setProperty("rate", 165)

def set_state(state: str):
    try:
        requests.post(f"{API_URL}/{state}")
    except:
        pass

def speak(text: str):
    if not text:
        return

    set_state("speaking")
    print("🗣️ CRONOS dice:", text)

    engine.say(text)
    engine.runAndWait()

    set_state("idle")

import speech_recognition as sr
import requests

API_URL = "http://localhost:8000/state"

recognizer = sr.Recognizer()
mic = sr.Microphone()

def set_state(state: str):
    try:
        requests.post(f"{API_URL}/{state}")
    except:
        pass

def listen():
    with mic as source:
        set_state("listening")
        print("🎤 Escuchando...")
        audio = recognizer.listen(source)

    set_state("thinking")

    try:
        text = recognizer.recognize_google(audio, language="es-ES")
        print("👂 Oído:", text)
        return text
    except Exception as e:
        print("❌ Error:", e)
        set_state("idle")
        return ""

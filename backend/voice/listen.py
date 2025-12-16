import speech_recognition as sr
from backend.core.state import set_state

recognizer = sr.Recognizer()
mic = sr.Microphone()

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

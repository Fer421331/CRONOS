from backend.voice.listen import listen
from backend.voice.speak import speak

def run():
    print("🧠 CRONOS INICIADO")
    while True:
        text = listen()
        if text:
            speak(f"Dijiste {text}")

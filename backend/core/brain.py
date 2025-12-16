from backend.voice.listen import listen
from backend.voice.speak import speak

def run():
    while True:
        text = listen()
        if text:
            speak(f"Dijiste {text}")

class Assistant:
    def __init__(self, name="Jarvis"):
        self.name = name

    def speak(self, text):
        print(f"{self.name}: {text}")

    def start(self):
        self.speak("System online. Voice assistant ready.")

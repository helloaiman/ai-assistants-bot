class Assistant:
    def __init__(self, name="Jarvis"):
        self.name = name
        self.running = True

    def speak(self, text):
        print(f"{self.name}: {text}")

    def listen(self):
        return input("You: ").strip().lower()

    def handle_command(self, command):
        if command in ["hi", "hello"]:
            self.speak("Hello. How can I help you?")
        elif command == "time":
            from datetime import datetime
            now = datetime.now().strftime("%H:%M")
            self.speak(f"The time is {now}")
        elif command in ["exit", "quit", "shutdown"]:
            self.speak("Shutting down. Goodbye.")
            self.running = False
        else:
            self.speak("Command not recognized.")

    def start(self):
        self.speak("System online. Awaiting commands.")
        while self.running:
            command = self.listen()
            self.handle_command(command)

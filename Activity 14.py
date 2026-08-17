import pyttsx3
from datetime import datetime
engine=pyttsx3.init()
def speak(text):
    engine.say(text)
    engine.runAndWait()
def respond_to_command(command):
    if "hello" in command:
        speak("Hi there! How can I help you today?")
    elif "your name" in command:
        speak("I am your Python voice assistant.")
    elif "time" in command:
        now = datetime.now().strftime("%H:%M")
        speak(f"The time is {now}")
    elif "what can you do" in command:
        speak("I can respond to simple commands.")
    elif "how are you" in command:
        speak("I'm doing great! Thanks for asking.")
    elif "exit" in command or "stop" in command:
        speak("Goodbye!")
        return False
    else:
        speak("I'm not sure how to help with that.")
    return True
while True:

    command = input("Enter your command:")

    if not respond_to_command(command):
        break
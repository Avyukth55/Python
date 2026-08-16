import pyttsx3
from googletrans import Translator
print("Available translation languages:")
print("1. Hindi")
print("2. Tamil")
print("3. Telugu")
print("4. Bengali")
print("5. Marathi")
print("6. Gujarati")
print("7. Malayalam")
print("8. Punjab")

languges = {
    "1." : "hi",
    "2." : "ta",
    "3." : "te",
    "4." : "bn",
    "5." : "mr",
    "6." : "gu",
    "7." : "ml",
    "8." : "pa"
}
choice = input("Choose a language:")
text= input("Enter a text in English")
language = languages.get(choice, "hi")
translated = Translator().translate(text, dest=language).text
print("Translation:", translated)
engine = pyttsx3.init()
engine.say(translated)
engine.runAndWait()
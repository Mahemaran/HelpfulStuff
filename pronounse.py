import pyttsx3

# Initialize the text-to-speech engine
engine = pyttsx3.init()
engine.setProperty('rate', 125)

# Text you want to pronounce
text = "Asynchronous "

# Speak the text
engine.say(text)
engine.runAndWait()

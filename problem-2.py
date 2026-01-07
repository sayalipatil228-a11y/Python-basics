import pyttsx3

engine = pyttsx3.init()
engine.say("Hello Sayali, pyttsx3 is working! you are awesome!")
engine.runAndWait()
engine.stop()
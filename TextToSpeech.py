import pyttsx3
speak=pyttsx3.init()
text=input("Write something: ")
speak.setProperty('rate', 125)
#------to make female voice
# voices = speak.getProperty('voices')
# speak.setProperty('voice', voices[1].id)
speak.say(text)
speak.runAndWait()
speak.stop()

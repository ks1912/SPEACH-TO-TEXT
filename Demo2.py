#Speak and print

import speech_recognition as sr


r1 = sr.Recognizer()

with sr.Microphone() as source:
    print('SPEAK WHAT YOU WANT TO SPEAK:')
    audio = r1.listen(source)
    r1.pause_threshold == "3"
try:
    text = r1.recognize_google(audio)
    print('WORD SPOKEN BY YOU ARE : {}'. format(text))
except:
    print("Could not recognize your voice")
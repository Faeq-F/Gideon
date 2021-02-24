import time
try:
    import speech_recognition as sr
except:
    time.sleep(0)

import datetime
import wikipedia
try:
    import webbrowser
    import wolframalpha
except:
    time.sleep(0)
import os
import subprocess
try:
    from ecapture import ecapture as ec
except:
    time.sleep(0)
try:
    import json
except:
    time.sleep(0)
import requests
#-------------------------------------
#engine=pyttsx3.init('sapi5')
#voices=engine.getProperty('voices')
#engine.setProperty('voice','voices[1].id')
#-------------------------------------
def speak(text):
    os.system("espeak "+str(text))
    #engine.runAndWait()
#-------------------------------------
def wishMe():
    hour=datetime.datetime.now().hour
    if hour>=0 and hour<12:
        speak('Hello, good morning Faykhe')
        print('Hello, good morning Faykhe')
    elif hour>=12 and hour<18:
        speak('Hello, good afternoon Faykhe')
        print('Hello, good afternoon Faykhe')
    else:
        speak('Hello, good evening Faykhe')
        print('Hello, good evening Faykhe')
#-------------------------------------
def takeCommand():
    r=sr.recognize_ibm()
    with sr.Microphone() as source:
        print("Listening...")
        audio=r.listen(source)

        try:
            statement=r.recognize_google(audio,language='en-in')
            print("user said:{ ", str(statement), "}\n")

        except Exception as e:
            speak("Sorry, please say that again")
            return "None"
        return statement

print("Loading Gideon resources")
speak("Loading Gideon's resources")
wishMe()
if __name__=='__main__':


    while True:
        speak("Tell me how can I help you now?")
        statement = takeCommand().lower()
        if statement==0:
            continue
        if "good bye" in statement or "ok bye" in statement or "stop" in statement:
            speak('your personal assistant G-one is shutting down,Good bye')
            print('your personal assistant G-one is shutting down,Good bye')
            break

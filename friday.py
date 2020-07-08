"""
    sudo apt-get update && sudo apt-get install espeak
    If there is an error
"""
import pyttsx3
import datetime
import speech_recognition as sr
import pyaudio
import wikipedia

engine = pyttsx3.init()

def speak(audio):
    engine.say(audio)
    engine.runAndWait()

def time():
    Time = datetime.datetime.now().strftime("%I:%M:%S")
    speak("the current time is")
    speak(Time)

def date():
    year = int(datetime.datetime.now().year)
    month = int(datetime.datetime.now().month)
    day = int(datetime.datetime.now().day)
    speak("The current date is")
    speak(day)
    speak(month)
    speak(year)

def wishme():
    speak("Welcome back sir!")
    time()
    date()
    speak("FRIDAY at your service, Please tell me how can I help you")

def takeCommand():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        r.pause_threshold = 1
        audio = r.listen(source)
    try:
        print("Recognizing...")
        query = r.recognize_google(audio, language='en-US')
        print(query)
    except Exception as e:
        print(e)
        speak("I couldn't understand you, could you please repeat that again...")
        takeCommand()

    return query

if __name__ == "__main__":
    wishme()
    while True:
        query = takeCommand().lower()

        if 'time' in query:
            time()
        elif 'date' in query:
            date()
        elif 'wikipedia' in query:
            speak('Searching...')
            query = query.replace('wikipedia', '')
            result = wikipedia.summary(query, sentences = 2)
            print(result)
            speak(result)
        elif 'offline' in query:
            quit()

import pyttsx3
import datetime
import speech_recognition as sr
import wikipedia
import webbrowser
import os
import random

engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[0].id)


def speak(audio):
    engine.say(audio)
    engine.runAndWait()


def wishMe():
    hour = int(datetime.datetime.now().hour)
    if hour>=0 and hour<12:
        speak("Good Morning")
    elif hour>=12 and hour<17:
        speak("Good Afternoon")
    else:
        speak("Good Evening")
    speak("I am Alan , What can i do for you sir?")


def takeCommand():
    # for taking microphone input and return string output
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        r.pause_threshold = 1
        audio = r.listen(source)
    try:
        print("Recognizing")
        query = r.recognize_google(audio,language='en-in')
        print(f"user said: {query}\n")

    except Exception as e:
        # print(e)
        print("say that again please...")
        return "none"
    return query



if __name__ == "__main__":
    wishMe()
    while True:
        query = takeCommand().lower()
        if 'wikipedia' in query:
            speak('Searching wikipedia')
            query = query.replace("wikipedia","")
            results = wikipedia.summary(query,sentences=2)
            speak("According to wikipedia")
            print(results)
            speak(results)

        elif 'open youtube' in query:
            speak("initiating request sir")
            webbrowser.open("youtube.com")

        elif 'open google' in query:
            speak("initiating request sir")
            webbrowser.open("google.com")

        elif 'open stackoverflow' in query:
            speak("initiating request sir")
            webbrowser.open("stackoverflow.com")

        elif 'play music' in query:
            speak("initiating request sir")
            music_dir = "H:\\Songs"
            songs = os.listdir(music_dir)
            os.startfile(os.path.join(music_dir,songs[random.randint(0,len(songs)-1)]))

        elif 'the time' in query:
            strTime = datetime.datetime.now().strftime("%H:%M:%S")
            speak(f"sir , the time is {strTime}")
            print(f"Sir, the time is {strTime}\n")

        elif 'open pycharm' in query:
            speak("initiating request sir")
            pycharmPath = "C:\\Program Files\\JetBrains\\PyCharm Community Edition 2020.1.1\\bin\\pycharm64.exe"
            os.startfile(pycharmPath)

        elif 'open opera' in query:
            speak("initiating request sir")
            operaPath = "C:\\Program Files (x86)\\Opera\\launcher.exe"
            os.startfile(operaPath)

        elif 'open spotify' in query:
            speak("initiating request sir")
            spotifyPath = "C:\\Users\\Abhiraj Rathore\\AppData\\Roaming\\Spotify\\Spotify.exe"
            os.startfile(spotifyPath)

        elif 'open chrome' in query:
            speak("initiating request sir")
            chromePath = "C:\\Program Files\\Google\\Chrome\\Application\\chrome.exe"
            os.startfile(chromePath)

        elif 'email to jerry' in query:
            try:
                speak("what should I say ?")
                content = takeCommand()
                to = "palaraa@gmail.com"
                sendEmail(to,content)
            except Exception as e:
                speak("sir i could not send email at this time")

        elif 'play movie' in query:
            speak("initiating request sir")
            movie_dir = "H:\\seen\\Random movies"
            movie = os.listdir(movie_dir)
            os.startfile(os.path.join(movie_dir,movie[random.randint(0,len(movie)-1)]))

        elif 'who are you' in query:
            speak("I am Alan named after the greatest mathematician Alan Turing . A program which was designed to be an assistant by mr. Abhiraj Rathore")

        elif 'what can you do' in query:
            speak("I can play a movie for you or even a song if you like. I can also search wikipedia for anything you want")
        elif 'good boy' in query:
            speak("Thanks sir , its an honor to serve you")

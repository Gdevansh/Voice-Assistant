import pyttsx3
import speech_recognition as sr
import datetime
import wikipedia
import webbrowser
import pywhatkit
import pyjokes
import pyaudio
engine = pyttsx3.init('sapi5')
voices=engine.getProperty('voices')
engine.setProperty('voice',voices[0].id)

webbrowser.register('chrome',
	None,
	webbrowser.BackgroundBrowser("C:\Program Files\Google\Chrome\Application//chrome.exe"))


def speak(audio):
    engine.say(audio)
    engine.runAndWait()

def user_commands():
    listener = sr.Recognizer()
    try:
        with sr.Microphone() as source:
            print("Start Speaking!!")
            voice = listener.listen(source)
            command = listener.recognize_google(voice)
            command = command.lower()
            if 'alexa' in command:
                command = command.replace('alexa', '')
                print(command)
    except:
        pass
    return command


def wishMe():
    hour = int(datetime.datetime.now().hour)
    if hour>=0 and hour<12:
        speak('Good Morning')
    elif hour>=12 and hour<18:
        speak('Good Afternoon')
    else:
        speak('Good Evening')


    speak('I am Jarvis . Please tell me how may I help you.')

def takeCommand():
        # It takes microphone input from the user and returns string output

    r = sr.Recognizer()
    with sr.Microphone() as source:
         print("Listening...")
         r.pause_threshold = 1
         audio = r.listen(source)
    try:
         print('Recgonizing....')
         query = r.recognize_google(audio, language='en-in')  # Using google for voice recognition.
         query=query.replace('Jarvis','')
         print(f"User said: {query}\n")  # User query will be printed.

    except Exception as e:
         # print(e)
         print("Say that again please...")  # Say that again will be printed in case of improper voice
         speak("Say that again please...")
         return "None"  # None string will be returned
    return query

if __name__ == "__main__":
    wishMe()
    while True:
        # if 1:
        query = takeCommand().lower()

        # Logic for executing tasks based on query
        if 'tell me about' in query:
            speak('Searching Wikipedia...')
            query = query.replace("tell me about", "")
            results = wikipedia.summary(query, sentences=2)
            speak("According to Wikipedia")
            print(results)
            speak(results)

        elif 'open youtube' in query:
            webbrowser.get('chrome').open_new("youtube.com")

        elif 'open google' in query:
            webbrowser.get('chrome').open_new("google.com")



        elif 'the time' in query:
            strTime = datetime.datetime.now().strftime("%I:%M:%p")
            speak(f"Sir, the time is {strTime}")

        elif 'play' in query:
            song = query.replace('play', '')
            print('Playing'+ song)
            speak('Playing' + song)
            pywhatkit.playonyt(song)
        elif 'joke' in query:
            print(pyjokes.get_joke())
            speak(pyjokes.get_joke())
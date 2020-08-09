import pyttsx3 #pip install pyttsx3
import speech_recognition as sr #pip install speechRecognition
import datetime
import wikipedia #pip install wikipedia
import webbrowser
import os
import smtplib

engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
# print(voices[1].id)
engine.setProperty('voice', voices[0].id)
engine.setProperty('rate', 175)


def speak(audio):
    engine.say(audio)
    engine.runAndWait()


def wishMe():
    hour = int(datetime.datetime.now().hour)
    if hour>=0 and hour<12:
        speak("Good Morning!")

    elif hour>=12 and hour<18:
        speak("Good Afternoon!")   

    else:
        speak("Good Evening!")  

    speak("HELLO , i m jarvis , speed 1 terahertz, memory 1 zettabyte and i am your naukar maalik")       

def takeCommand():
    #It takes microphone input from the user and returns string output

    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        r.pause_threshold = 1
        r.energy_threshold = 100
        audio = r.listen(source)

    try:
        print("Recognizing...")    
        query = r.recognize_google(audio, language='en-in')
        print(f"User said: {query}\n")

    except Exception as e:   
        print("Say that again please...")
        # speak("Say that again please...") 
        print(e) 
        return "None"
    return query

def sendEmail(to, content):
    server = smtplib.SMTP('smtp.gmail.com', 587)
    server.ehlo()
    server.starttls()
    server.login('youremail@gmail.com', 'your-password')
    server.sendmail('youremail@gmail.com', to, content)
    server.close()

if __name__ == "__main__":
    wishMe()
    while True:
        query = takeCommand().lower()

        # Logic for executing tasks based on query
        if 'wikipedia' in query:
            speak('Searching Wikipedia...')
            query = query.replace("wikipedia", "")
            results = wikipedia.summary(query, sentences=2)
            speak("According to Wikipedia")
            print(results)
            speak(results)

        elif 'open youtube' in query:
            speak("opening youtube sir!")
            c = webbrowser.get() 
            c.open('http://www.youtube.com')

        elif 'open google' in query:
            speak("opening google sir!")
            c = webbrowser.get() 
            c.open('http://www.google.com')

        elif 'open stackoverflow' in query:
            speak("opening stackowerflow sir!")
            c = webbrowser.get() 
            c.open('http://www.stackoverflow.com')


        elif 'play music' in query:
            speak("playing music sir!")
            music_dir = 'F:\\New folder\\XBabbu Maan'
            songs = os.listdir(music_dir)
            print(songs)    
            os.startfile(os.path.join(music_dir, songs[0]))

        elif 'the time' in query:
            strTime = datetime.datetime.now().strftime("%H:%M:%S")    
            speak(f"Sir, the time is {strTime}")

        elif 'open code' in query:
            codePath = "C:\\Users\\J.A.R.V.I.S\\AppData\\Local\\Programs\\Microsoft VS Code\\Code.exe"
            os.startfile(codePath)

        elif 'who are you' in query:
            speak("Hello, I'm Jarvis, speed 1 Terabyte, memory 1 zettabyte")
        
        elif 'thank you' in query:
            speak("its my pleasure sir!")
            exit()
        elif 'opera' in query:
            codePath = "C:\\Users\\J.A.R.V.I.S\\AppData\\Local\\Programs\\Opera\\launcher.exe"
            os.startfile(codePath)

        elif 'email to harry' in query:
            try:
                speak("What should I say?")
                content = takeCommand()
                to = "yourEmail@gmail.com"    
                sendEmail(to, content)
                speak("Email has been sent!")
            except Exception as e:
                print(e)
                speak("Sorry my friend harry. I am not able to send this email")    

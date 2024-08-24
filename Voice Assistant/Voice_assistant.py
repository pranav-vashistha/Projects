import pyttsx3  # pip install pyttsx3
import speech_recognition as sr  # pip install speechRecognition
import datetime  # imported date and time
import webbrowser  # imported webbrowser
import time  # for using real time related functons
import subprocess  # for system operations
import ecapture as ec  # for opening camera from code
import pyjokes  # for telling jokes
 
# importing default voice from pyttsx3 library
engine = pyttsx3.init('sapi5')  # name of voice module
voices = engine.getProperty('voices')
 
# setting property of voice assitant
engine.setProperty('voice', voices[0].id)  
 
# function for speaking audio we will use speak for using our va
def speak(audio):
    engine.say(audio)
    engine.runAndWait()
 
# Defining function where va will wish us on time.
def wishMe():
    hour = int(datetime.datetime.now().hour)
    if hour >= 0 and hour < 12:
        # if morning then va will wish good morning
        speak("Good Morning!")  
 
    elif hour >= 12 and hour < 18:
        # same for good afternoon
        speak("Good Afternoon!")  
 
    else:
        # same for good evening
        speak("Good Evening!")  
        
    #used to tell the system what to speak
    speak("Hello Ankit sir, i am your personal voice assistant")
    speak('What would you like me to do?')
 
# It takes microphone input from the user and returns string output
 
def takeCommand():
    # speech recognition function
    r = sr.Recognizer()  
    # for using microphone from our system
    with sr.Microphone() as source:  
        print("Listening...")
        # pause time for listening
        r.pause_threshold = 1  
        # storing data of source in audio
        audio = r.listen(source)  
 
    try:
        print("Recognizing...")
        # for recognising english language
        query = r.recognize_google(audio, language='en-in')
        # printing what user said by recognizing speech
        print(f"User said: {query}\n")
        
        
    # if speech recognition doesnt get meanigful data then it throws this message
    except Exception as e:  
        speak("I cant understand can you Say that again please?")
        return "None"
    return query
 
 
# defining logic by which we can implement tasks.
if __name__ == "__main__":  # main function
    wishMe()
    while True:  # infinite loop for continuous use
        # we will take voice in lower case
        query = takeCommand().lower()  
 
        # Logic for executing tasks based on query
 
        if 'open youtube' in query:
            # webbrowser library for excessing browser
            webbrowser.open("https://www.youtube.com/")
 
        elif 'open nirma mail' in query:
            webbrowser.open("https://mail.google.com/mail/u/1/#inbox")
 
        elif 'open google' in query:
            webbrowser.open("https://www.google.co.in")
 
        elif 'what is the time' in query:
            strTime = datetime.datetime.now().strftime(
                "%H:%M:%S")  
            # used time library for displaying time
            speak(f"Sir, the time is {strTime}")
 
        elif 'how are you' in query:
            speak('I am fine sir')
 
        elif 'ok bye' in query:
            speak('Ok sir, have a nice day')
            break
 
        elif 'hey jarvis' in query:
            speak('Yes sir?')
        
        # used subprocess library to access internal settings of system
        elif 'shutdown system' in query:  
            speak("Hold On a Sec ! Your system is on its way to shut down")
            subprocess.call('shutdown / p /f')
            
        # time library used for counting real time
        elif "don't listen" in query or "stop listening" in query:  
            speak("for how much time you want to stop jarvis from listening commands")
            a = int(takeCommand())
            time.sleep(a)
            print(a)
 
        elif "who are you" in query:
            speak("I am your virtual assistant Pranav Vashistha")
            
        # ecapture library to open camera and take photo
        elif "take a photo" in query or "Camera" in query:  
            ec.capture(0, "Jarvis Camera ", "img.jpg")
        
        # we used pyjokes library to get a joke from our va
        elif "tell me joke" in query:  
            speak(pyjokes.get_joke())

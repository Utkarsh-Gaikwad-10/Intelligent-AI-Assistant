# Import necessary modules for the voice assistant

import datetime     # Module to work with date and time
import pyttsx3      # Text-to-speech library for voice output
import speech_recognition as sr   # Speech recognition library for voice input
import wikipedia     # Access Wikipedia for information
import webbrowser      # Open web pages in the default web browser
import os           # Access and execute system files and commands
import pyjokes         # Generate and tell jokes
import requests         # Send HTTP requests and handle responses
import sys
import operator
import pyautogui
import time

# Initialize the text-to-speech engine
engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[0].id)

# Function to speak a given text
def speak(audio):
    engine.say(audio)
    engine.runAndWait()


# Function to greet the user based on the time of day
def wishMe():
    hour = int(datetime.datetime.now().hour)
    if hour>=0 and hour<12:
        speak("Good Morning Sir !!")

    elif hour>=12 and hour<18:
        speak("Good Afternoon Sir !!")

    else:
        speak("Good Evening Sir !!")

    speak("I am Nova your AI assistant . please tell me how may i help you")

# Function to listen to user's voice command
def takeCommand():
    # it takes microphone input from the user and returns string output
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        r.pause_threshold = 0.8
        audio = r.listen(source)

    try:
        print("Recognizing...")
        query = r.recognize_google(audio, language='en-in')
        print(f"User said: {query}\n")

    except Exception as e:     # If there's an error in recognizing the speech, ask the user to repeat
        #print(e)
        print("Say that again please...")
        return "None"
    return query

if __name__ == "__main__":
    wishMe()
    while True:
        query = takeCommand().lower()

        if 'wikipedia' in query:     # Command to search on Wikipedia
            speak("Searching Wikipedia...")
            query = query.replace("wikipedia", "")
            results = wikipedia.summary(query, sentences = 2)
            speak("According to Wikipedia")
            print(results)
            speak(results)

        elif 'how are you ' in query:      # Greeting response
            speak("i am fine sir. thanks about asking. how are you doing")

        elif 'open youtube' in query:       # Command to open YouTube
            speak("opening you tube")
            webbrowser.open("youtube.com")

        elif 'open google' in query:         # Command to open google
            speak("opening google")
            webbrowser.open("google.com")

        elif 'play music' in query:           # Command to play music
            music_dir = 'D:\\Songs'
            songs = os.listdir(music_dir)
            print(songs)
            os.startfile(os.path.join(music_dir, songs[0]))

        elif 'the time' in query:             # Command to get the current time
            strTime = datetime.datetime.now().strftime("%H:%M:%S")
            speak(f"sir, the time is {strTime}")

        elif 'open code' in query:
            codePath = "C:\\Users\\Dream\\AppData\\Local\\Programs\\Microsoft VS Code\\Code.exe"
            os.startfile(codePath)

        elif 'joke' in query:             # Command to tell a joke
            speak(pyjokes.get_joke())

        elif 'news' in query:              # Command to open news website
            news = webbrowser.open_new_tab("https://timesofindia.indiatimes.com")
            speak('Here are some headlines from the Times of India, Happy reading')

        elif 'open facebook' in query:       # Command to open facebook
            speak('Opening Facebook')
            webbrowser.open("https://www.facebook.com")

        elif 'open instagram' in query:        # Command to open instagram
            speak('Opening instagram')
            webbrowser.open("https://www.instagram.com/explore/?hl=en")

        elif 'open linkedin' in query:         # Command to open linkedin
            speak("opening linkedin")
            webbrowser.open("https://www.linkedin.com")


        elif 'open chat gpt' in query:           # Command to open chatgpt
            speak("opening chat gpt")
            webbrowser.open("https://gemini.google.com")

        elif 'open microsoft word' in query:        # Command to open microsoft word
            speak("opening microsoft word")
            os.startfile("C:\ProgramData\Microsoft\Windows\Start Menu\Programs\Microsoft Office\Microsoft Word 2010.lnk")


        elif 'open microsoft excel' in query:         # Command to open excel
            speak("opening microsoft excel")
            os.startfile("C:\ProgramData\Microsoft\Windows\Start Menu\Programs\Microsoft Office\Microsoft Excel 2010.lnk")


        elif 'open microsoft powerpoint' in query:      # Command to open powerpoint
            speak("opening microsoft powerpoint")
            os.startfile("C:\ProgramData\Microsoft\Windows\Start Menu\Programs\Microsoft Office\Microsoft PowerPoint 2010.lnk")

        elif 'search on youtube' in query:      # Command to search on youtube
            query = query.replace("search on youtube", "")
            webbrowser.open(f"www.youtube.com/results?search_query={query}")

        elif 'open microsoft edge' in query:      # Command to open microsoft edge
            speak("opening microsoft edge")
            os.startfile("C:\Program Files (x86)\Microsoft\Edge\Application\msedge.exe")

        elif 'close microsoft edge' in query:    # Command to close Microsft Edge
            os.system("taskkill /f /im msedge.exe")

        elif "shut down" in query:
            os.system("shutdown /s /t 5")

        elif "restart the system" in query:
            os.system("shutdown /r /t 5")

        elif "open command prompt" in query:
            os.system("start cmd")

        elif "close command prompt" in query:
            os.system("taskkill /f /im cmd.exe")

        elif "stop running the code" in query:
            speak('Code Stopped')
            sys.exit()


        
        elif "calculate" in query:
            r = sr.Recognizer()
            with sr.Microphone() as source:
                speak("ready")
                print("Listening...")
                r.adjust_for_ambient_noise(source)
                audio = r.listen(source)
            my_string=r.recognize_google(audio)
            print(my_string)
            def get_operator_fn(op):
                return {
                    '+' : operator.add,
                    '-' : operator.sub,
                    'x' : operator.mul,
                    'divided' : operator.__truediv__,
                }[op]
            def eval_bianary_expr(op1,oper, op2):
                op1,op2 = int(op1), int(op2)
                return get_operator_fn(oper)(op1, op2)
            speak("your result is")
            speak(eval_bianary_expr(*(my_string.split())))

        elif "what is my ip address" in query:
            speak("Checking")
            try:
                ipAdd = requests.get('https://api.ipify.org').text
                print(ipAdd)
                speak("your ip address is")
                speak(ipAdd)
            except Exception as e:
                speak("network is weak, please try again some time later")

        elif "volume up" in query:
            pyautogui.press("volumeup")
            pyautogui.press("volumeup")
            pyautogui.press("volumeup")
            pyautogui.press("volumeup")
            pyautogui.press("volumeup")
            pyautogui.press("volumeup")
            pyautogui.press("volumeup")
            pyautogui.press("volumeup")
            pyautogui.press("volumeup")
            pyautogui.press("volumeup")
            pyautogui.press("volumeup")
            pyautogui.press("volumeup")

        elif "volume down" in query:
            pyautogui.press("volumedown")
            pyautogui.press("volumedown")
            pyautogui.press("volumedown")
            pyautogui.press("volumedown")
            pyautogui.press("volumedown")
            pyautogui.press("volumedown")
            pyautogui.press("volumedown")
            pyautogui.press("volumedown")

        elif "mute" in query:
            pyautogui.press("volumemute")

        elif "scroll down" in query:
            pyautogui.scroll(1000)

        
        elif "your name and purpose" in query:
            print('My Name Is Nova')
            speak('My Name Is Nova')
            print('I can Do Everything that my creator programmed me to do')
            speak('I can Do Everything that my creator programmed me to do')

        elif 'maximize this window' in query:
            pyautogui.hotkey('alt', 'space')
            time.sleep(1)
            pyautogui.press('x')

        elif 'open new window' in query:
            pyautogui.hotkey('ctrl', 'n')

        elif 'open incognito window' in query:
            pyautogui.hotkey('ctrl', 'shift', 'n')

        elif 'minimise this window' in query:
            pyautogui.hotkey('alt', 'space')
            time.sleep(1)
            pyautogui.press('n')
        
        elif 'open history' in query:
            pyautogui.hotkey('ctrl', 'h')

        elif 'open downloads' in query:
            pyautogui.hotkey('ctrl', 'j')

        elif 'previous tab' in query:
            pyautogui.hotkey('ctrl', 'shift', 'tab')
        
        elif 'next tab' in query:
            pyautogui.hotkey('ctrl', 'tab')
 
        elif 'close tab' in query:
            pyautogui.hotkey('ctrl', 'w')
 
        elif 'close window' in query:
            pyautogui.hotkey('ctrl', 'shift', 'w')

        elif 'clear browsing history' in query:
            pyautogui.hotkey('ctrl', 'shift', 'delete')








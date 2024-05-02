import pyttsx3
import datetime
import speech_recognition as sr
import wikipedia
import webbrowser
import pywhatkit as kit
import os
import cv2
import pyautogui





def takeCommand():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print('Listening')
        r.pause_threshold = 0.7
        audio = r.listen(source)

        try:
            print("Recognizing")
            Query = r.recognize_google(audio, language='en-in')
            print("the command is printed=", Query)

        except Exception as e:
            print(e)
            print("Say that again sir")
            return "None"

        return Query

def wishMe():
   hour = int(datetime.datetime.now().hour)
   if hour>=0 and hour<12:
     speak("Good Morning!")
   elif hour>=12 and hour<18:
     speak("Good Afternoon!") 
   else:
     speak("Good Evening!")

   speak("Ready To Comply. What can I do for you ?")
def speak(audio):
    engine = pyttsx3.init()
    voices = engine.getProperty('voices')
    engine.setProperty('voice', voices[0].id)
    engine.say(audio)
    engine.runAndWait()


def tellDay():
    day = datetime.datetime.today().weekday() + 1
    Day_dict = {1: 'Monday', 2: 'Tuesday', 3: 'Wednesday', 4: 'Thursday', 5: 'Friday', 6: 'Saturday', 7: 'Sunday'}

    if day in Day_dict.keys():
        day_of_the_week = Day_dict[day]
        print(day_of_the_week)
        speak("The day is " + day_of_the_week)


def tellTime():
    time = str(datetime.datetime.now())
    print(time)
    hour = time[11:13]
    min = time[14:16]
    speak("The time is sir" + hour + "Hours and" + min + "Minutes")


def Hello():
    speak("hello  Mr. Adarsha Routray , I am your desktop assistant. Tell me how may I help you")


def Take_query():
    Hello()

    while(True):
        query = takeCommand().lower()

        if 'jarvis' in query:
            print('Yes Adarsh')
            speak('Yes Adarsh')
        elif "who are you" in query:
            print('My Name Is JIA')
            speak('My Name Is JIA')
            print('I can Do Everything that my creator programmed me to do')
            speak('I can Do Everything that my creator programmed me to do')
        elif "who created you" in query:
            print('ADARSH MADE ME , I created with Python Language, in Visual Studio Code.')
            speak('ADARSH, I created with Python Language, in Visual Studio Code.')
      

        if "open geeksforgeeks" in query:
            speak("Opening GeeksforGeeks ")
            webbrowser.open("www.geeksforgeeks.com")
            continue

        elif "open google" in query:
            speak("Opening Google ")
            webbrowser.open("www.google.com")
            continue

        elif "which day it is" in query:
            tellDay()
            continue

        elif "tell me the time" in query:
            tellTime()
            continue

        elif "bye" in query:
            speak("Bye. Check Out GFG for more exciting things")
            exit()

        elif "from wikipedia" in query:
            speak("Checking the wikipedia ")
            query = query.replace("wikipedia", "")
            result = wikipedia.summary(query, sentences=4)
            speak("According to wikipedia")
            speak(result)

        elif "tell me your name" in query:
            speak("I am Jarvis. Your desktop Assistant")

        elif 'open youtube' in query:
            speak("Opening YouTube")
            webbrowser.open("www.youtube.com")
            continue
        if 'play music' in query:
            speak("Playing music")
            music_dir = 'C:\\Users\\KIIT\\Music\\Bhajan'
            songs = os.listdir(music_dir)
            if len(songs) == 0:
                speak("No music files found")
            else:
                os.startfile(os.path.join(music_dir, songs[0]))  # Play the first song in the directory

        elif 'exit' in query:
            speak("Exiting")
            break
        elif "open camera" in query:
            cap = cv2.VideoCapture(0)
            while True:
                ret, img = cap.read()
                cv2.imshow('webcam', img)
                k = cv2.waitKey(50)
                if k==27:
                    break;
                    cap.release()
                    cv2.destroyAllWndows()
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
            pyautogui.press("volumedown")
            pyautogui.press("volumedown")
            pyautogui.press("volumedown")
            pyautogui.press("volumedown")
            pyautogui.press("volumedown")
            pyautogui.press("volumedown")
            pyautogui.press("volumedown")
        elif "mute" in query:
            pyautogui.press("volumemute")
  

if __name__ == '__main__':
    Take_query()

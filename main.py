import time
import pyttsx3  #pip install pyttsx3
import speech_recognition as sr #pip install speechRecognition
import datetime
import wikipedia #pip install wikipedia
import webbrowser
import os
import smtplib
from selenium import  webdriver
from logger import customelog

logger = customelog()


class Desktop_Assistant:
   def __init__(self):
       try:
           self.engine = pyttsx3.init('sapi5')
           self.voices = self.engine.getProperty('voices')
           # print(voices[1].id)
           self.engine.setProperty('voice', self.voices[1].id)
           logger.loginfo("Initialized Object of Desktop Assistant")
       except Exception as e:
           print(e)
   def speak(self, audio):
       try:
           self.engine.say(audio)
           self.engine.runAndWait()
       except Exception as e :
           print(e)

   def wishMe(self):
       try:
           hour = int(datetime.datetime.now().hour)
           if hour >= 0 and hour < 12:
               self.speak("Good Morning!")

           elif hour >= 12 and hour < 17:
               self.speak("Good Afternoon!")

           else:
               self.speak("Good Evening!")

           self.speak("I am Aleena . Please tell me how may I help you Sir")
       except Exception as e:
           print(e)
   def takeCommand(self):
       # It takes microphone input from the user and returns string output

       r = sr.Recognizer()
       with sr.Microphone() as source:
           print("Listening...")
           r.pause_threshold = 1
           audio = r.listen(source)

       try:
           print("Recognizing...")
           query = r.recognize_google(audio, language='en-in')
           print(f"User said: {query}\n")

       except Exception as e:
           # print(e)
           self.speak("Sir Say that again please...")
           print("Say that again please...")
           return "None"
       return query

   def sendEmail(self, to, content):
       server = smtplib.SMTP('smtp.gmail.com', 587)
       server.ehlo()
       server.starttls()
       gmail = 'chitterohit2112@gmail.com'
       password = 'Kalaam3@lpha'
       server.login(gmail, password)
       server.sendmail(gmail, to, content)
       server.close()

try:
    Assistant = Desktop_Assistant()
    Assistant.wishMe()

    while True:
        # if 1:
        query = Assistant.takeCommand().lower()

        # Logic for executing tasks based on query
        if 'wikipedia' in query:
            Assistant.speak('Searching Wikipedia...')
            query = query.replace("wikipedia", "")
            results = wikipedia.summary(query, sentences=2)
            Assistant.speak("According to Wikipedia")
            print(results)
            Assistant.speak(results)

        elif 'open youtube' in query:
            webbrowser.open("youtube.com")

        elif 'open google' in query:
            webbrowser.open("google.com")

        #elif 'open stackoverflow' or 'open stack overflow' in query:
        elif 'open stackoverflow' in query:
            webbrowser.open("stackoverflow.com")


        elif 'play music' in query:
            #music_dir = 'D:\\Non Critical\\songs\\Favorite Songs2'
            music_dir = 'R:\Redmi note 4 backup\music'
            songs = os.listdir(music_dir)
            print(songs)
            os.startfile(os.path.join(music_dir, songs[0]))

        elif 'the time' in query:
            strTime = datetime.datetime.now().strftime("%H:%M:%S")
            Assistant.speak(f"Sir, the time is {strTime}")

        elif 'open code' in query:
            codePath = "C:\\Users\\Haris\\AppData\\Local\\Programs\\Microsoft VS Code\\Code.exe"
            os.startfile(codePath)

        elif 'your name' in query:
            Assistant.speak("My name is aleena ,I'am a computer program")

        elif 'created you' in query:
            Assistant.speak("Rohit Chitte created me")

        elif 'send email' in query:
            try:
                Assistant.speak("What should I say?")
                content = Assistant.takeCommand()
                to = "kolhe_prajwal.ai@ghrce.raisoni.net"
                Assistant.sendEmail(to, content)
                Assistant.speak("Email has been sent!")
            except Exception as e:
                print(e)
                Assistant.speak("Sorry my friend harry bhai. I am not able to send this email")

        elif 'weather' in query:
            while True:
                try:
                    Assistant.speak("Please Say city name")
                    city = Assistant.takeCommand().lower()
                    print(city)
                    Assistant.speak("Searching for Weather Report")
                except Exception as e:
                    continue
                else:
                    break
            try:
                driver = webdriver.Chrome()
                driver.get("https://www.weather-forecast.com/locations/" + city + "/forecasts/latest")
                report = (driver.find_elements_by_class_name("b-forecast__table-description-content")[0].text)
                Assistant.speak("According to Report")
                print(report)
                Assistant.speak(f"Weather of {city} is {report}")
                time.sleep(1)
                Assistant.speak("Next Command Please")
            except Exception as e:
                print(e)

        elif 'stop listening' in query:
            break
except Exception as e:
    print(e)
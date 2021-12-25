import time
import pyttsx3  #pip install pyttsx3
import speech_recognition as sr #pip install speechRecognition
import datetime
import wikipedia #pip install wikipedia
import webbrowser
import os
import smtplib
from selenium import  webdriver
from logger import App_Logger
from tkinter import *              #For the graphics
from _tkinter import *
from DBoperations import MongoDBManagement

#intitiating logger classs object
try:
    logger = App_Logger()
except Exception as e:
    print(e)

#Initiating Database Object.
try:
    obj = MongoDBManagement("test","test")
    Database = obj.createDatabase("Female_Jarvis_Logs")
    Collection = obj.createCollection("Logs","Female_jarvis_Logs")
    obj.insertRecord("Female_Jarvis_Logs","Logs",{"Log":"Initiating The Project"})
except Exception as e:
    print(e)



class Desktop_Assistant:
   def __init__(self):
       try:
           self.engine = pyttsx3.init('sapi5')
           self.voices = self.engine.getProperty('voices')
           # print(voices[1].id)
           self.engine.setProperty('voice', self.voices[1].id)
          # logger.loginfo("Initialized Object of Desktop Assistant")
       except Exception as e:
           print(e)
           # logger.logerror("error occured while Initializing Object of Desktop Assistant")
   def speak(self, audio):
       try:
           self.engine.say(audio)
           self.engine.runAndWait()
           #logger.loginfo("executed speak function")
       except Exception as e :
           print(e)
           #logger.logerror("Error occured while executing speak funtion")

   def wishMe(self):
       try:
           hour = int(datetime.datetime.now().hour)
           if hour >= 0 and hour < 12:
               self.speak("Good Morning!")
               # logger.loginfo("wished Good Morning")

           elif hour >= 12 and hour < 17:
               self.speak("Good Afternoon!")
               #  logger.loginfo("wished Good Afternoon")

           else:
               self.speak("Good Evening!")
               # logger.loginfo("wished Good Evening")

           self.speak("I am female Jarvis . Please tell me how may I help you Sir")
           #  logger.loginfo("wishMe function executed successfully")
       except Exception as e:
           print(e)
           #  logger.logerror("Error occured while running wishme function")

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
           # logger.loginfo("takeCommand Function executed succesfully")
       except Exception as e:
           # print(e)
           self.speak("Sir Say that again please...")
           print("Say that again please...")
           return "None"
           # logger.logwarning("system was not able to recognise user audio input")
       #  logger.loginfo(f"user's query {query}")
       return query

   def sendEmail(self, to, content):
       try:
           server = smtplib.SMTP('smtp.gmail.com', 587)
           server.ehlo()
           server.starttls()
           gmail = 'chitterohit2112@gmail.com'
           password = 'Kalaam3@lpha'
           server.login(gmail, password)
           server.sendmail(gmail, to, content)
           server.close()
       except Exception as e:
           print(e)
           #   logger.logerror("Error Occured while executing sendEmail function")

try:

    Assistant = Desktop_Assistant()
    Assistant.wishMe()
except Exception as e:
    print(e)


def FemaleJarvis():
    while True:
        # if 1:
        try:
            query = Assistant.takeCommand().lower()
        except Exception as e:
            print(e)
        # Logic for executing tasks based on query
        try :


            if 'wikipedia' in query:
                try:
                    Assistant.speak('Searching Wikipedia...')
                    query = query.replace("wikipedia", "")
                    results = wikipedia.summary(query, sentences=2)
                    Assistant.speak("According to Wikipedia")
                    print(results)
                    Assistant.speak(results)
                except Exception as e:
                    print(e)


            elif 'open youtube' in query:
                try:
                    Assistant.speak("Opening youtube")
                    webbrowser.open("youtube.com")
                except Exception as e:
                    print(e)

            elif 'open google' in query:
                try:
                    Assistant.speak("Opening Google")
                    webbrowser.open("google.com")
                except Exception as e:
                    print(e)
            #elif 'open stackoverflow' or 'open stack overflow' in query:

            elif 'stack overflow' in query:
                try:
                    Assistant.speak("Opening Stackoverflow")
                    webbrowser.open("stackoverflow.com")
                except Exception as e:
                    print(e)

            elif 'play music' in query:
                try:
                    Assistant.speak("Playing Music")
                    #music_dir = 'D:\\Non Critical\\songs\\Favorite Songs2'
                    music_dir = 'R:\Redmi note 4 backup\music'
                    songs = os.listdir(music_dir)
                    print(songs)
                    os.startfile(os.path.join(music_dir, songs[0]))
                except Exception as e:
                    print(e)

            elif 'the time' in query:
                try:
                    strTime = datetime.datetime.now().strftime("%H:%M:%S")
                    Assistant.speak(f"Sir, the time is {strTime}")
                except Exception as e:
                    print(e)

            elif 'open code' in query:
                try:
                    Assistant.speak("Opening Visual Studio Code")
                    codePath = "C:\\Users\\Haris\\AppData\\Local\\Programs\\Microsoft VS Code\\Code.exe"
                    os.startfile(codePath)
                    #Assistant.speak("Next Command Please")
                except Exception as e:
                    print(e)

            elif 'your name' in query:
                try:
                    Assistant.speak("My name is Female Jarvis ,I'am a computer program")
                    #Assistant.speak("Next Command Please")
                except Exception as e:
                    print(e)

            elif 'created you' in query:
                try:
                    Assistant.speak("Rohit Chitte created me")
                    #Assistant.speak("Next Command Please")
                except Exception as e:
                    print(e)

            elif 'send email' in query:
                try:
                    Assistant.speak("What should I say?")
                    content = Assistant.takeCommand()
                    to = "kolhe_prajwal.ai@ghrce.raisoni.net"
                    Assistant.sendEmail(to, content)
                    Assistant.speak("Email has been sent!")
                    #Assistant.speak("Next Command Please")
                except Exception as e:
                    print(e)
                    Assistant.speak("Sorry my friend Rohit bhai. I am unable to send this email")


            elif 'terminate' in query:
                break

            """
            elif 'weather' in query:
    
                while True:
                    try:
                        Assistant.speak("Please Say city name")
                        city = Assistant.takeCommand().lower()
                        print(city)
                      #  Assistant.speak("Searching for Weather Report")
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
                    #Assistant.speak("Next Command Please")
    
                except Exception as e:
                    print(e)
            """
            Assistant.speak("Next Command Please")
        except Exception as e :
            print(e)
            break
    return

#name_file = open("R:\Machine learning\Full Stack DataScience iNeuron\Internship\Chota jarvis\A-GUI-Virtual-Assistant-with-python\Assistant_name", "r")
#name_assistant = name_file.read()
name_assistant = "femalejarvis"
def main_screen():
    global screen
    screen = Tk()
    screen.title(name_assistant)
    screen.geometry("100x250")
    screen.iconbitmap('app_icon.ico')

    name_label = Label(text=name_assistant, width=300, bg="black", fg="white", font=("Calibri", 13))
    name_label.pack()

    microphone_photo = PhotoImage(file="assistant_logo.png")
    microphone_button = Button(image=microphone_photo, command=FemaleJarvis)
    microphone_button.pack(pady=10)

    #settings_photo = PhotoImage(file="R:\Machine learning\Full Stack DataScience iNeuron\Internship\Ask Me any thing\settings.png")
    #settings_button = Button(image=settings_photo, command=change_name_window)
    #settings_button.pack(pady=10)

    #info_button = Button(text="Info", command=info)
    #info_button.pack(pady=10)

    screen.mainloop()


main_screen()



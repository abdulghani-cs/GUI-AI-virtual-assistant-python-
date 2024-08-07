import pyttsx3
import pyjokes
import datetime
import speech_recognition as sr
import wikipedia
import webbrowser
import random
import os
import smtplib
from googletrans import Translator
import requests
from bs4 import BeautifulSoup
from PyQt5 import QtWidgets, QtGui
from PyQt5.QtWidgets import QApplication, QMainWindow, QLabel, QPushButton
from PyQt5.QtGui import QPixmap
import sys

# Initialize the pyttsx3 engine
engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[0].id)

def speak(audio):
    engine.say(audio)
    engine.runAndWait()

def wishMe():
    hour = datetime.datetime.now().hour
    if hour >= 0 and hour < 12:
        speak("Good morning")
    elif hour >= 12 and hour < 18:
        speak("Good afternoon")
    else:
        speak("Good evening")
    speak("I am Abdulghani sir. Please tell me how may I help you.")

def takeCommand():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("----listening-----")
        r.pause_threshold = 1
        audio = r.listen(source)
    try:
        print("recognizing")
        query = r.recognize_google(audio, language='en-in')  
        print(f"User said: {query}\n")
        return query.lower()
    except Exception as e:
        print("Say that again please...")
        return ""

def playRandomMusic():
    music_urls = [
        "https://www.youtube.com/watch?v=5qap5aO4i9A",  # Lo-fi hip hop
        "https://www.youtube.com/watch?v=JGwWNGJdvx8",  # Shape of You
        "https://www.youtube.com/watch?v=kJQP7kiw5Fk",  # Despacito
        "https://www.youtube.com/watch?v=hT_nvWreIhg",  # Faded
        "https://www.youtube.com/watch?v=60ItHLz5WEA",  # Alan Walker - Alone
        "https://www.youtube.com/watch?v=PjJ0Ec1ErKg"   # New music link
    ]
    selected_music = random.choice(music_urls)
    webbrowser.open(selected_music)

def sendEmail(to, content):
    try:
        server = smtplib.SMTP('smtp.gmail.com', 587)
        server.ehlo()
        server.starttls()
        email = "ghaniimam5@gmail.com"
        app_password = "ahwt adna uvoj xxpj" 
        server.login(email, app_password)
        server.sendmail(email, to, content)
        server.close()
        speak("Email has been sent!")
    except Exception as e:
        print(e)
        speak("Sorry my friend abdulghani bhai. I am not able to send this email")

def translateText(text, dest_language):
    translator = Translator()
    translated = translator.translate(text, dest=dest_language)
    return translated.text

def getLanguageCode(language):
    language = language.lower()
    language_codes = {
        'arabic': 'ar',
        'urdu': 'ur',
        'english': 'en',
        'spanish': 'es',
        'french': 'fr',
        'german': 'de',
        'italian': 'it',
        'portuguese': 'pt',
        'russian': 'ru',
        'chinese': 'zh-cn',
        'japanese': 'ja',
        'korean': 'ko'
    }
    return language_codes.get(language, 'en')  

def getWeather(city):
    url = f"https://www.google.com/search?q=weather+in+{city}"
    response = requests.get(url)
    soup = BeautifulSoup(response.text, 'html.parser')
    weather_elem = soup.find('div', class_='BNeawe iBp4i AP7Wnd')
    if weather_elem:
        return weather_elem.text
    else:
        return "Weather information not found."

class VirtualAssistantGUI(QMainWindow):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        self.setWindowTitle("Virtual Assistant")
        self.setGeometry(100, 100, 800, 600)

        # Load background image
        self.bg_image = QPixmap("assistant.jpg")
        self.bg_label = QLabel(self)
        self.bg_label.setPixmap(self.bg_image)
        self.bg_label.resize(800, 600)

        # Add a button to start the assistant
        self.start_button = QPushButton('Start Listening', self)
        self.start_button.setGeometry(300, 500, 200, 50)
        self.start_button.setStyleSheet("background-color: blue; color: white; font-size: 14pt;")
        self.start_button.clicked.connect(self.startListening)

        # Wish the user
        wishMe()

    def startListening(self):
        query = takeCommand()
        self.handleCommand(query)

    def handleCommand(self, query):
        if 'wikipedia' in query:
            speak('Searching Wikipedia...')
            query = query.replace("wikipedia", "")
            results = wikipedia.summary(query, sentences=2)
            speak("According to Wikipedia")
            print(results)
            speak(results)
        elif 'open youtube' in query:
            webbrowser.open("https://www.youtube.com")
        elif 'open google' in query:
            webbrowser.open("https://www.google.com")
        elif 'open stackoverflow' in query:
            webbrowser.open("https://stackoverflow.com")
        elif 'open coursera' in query:
            webbrowser.open("https://www.coursera.org")
        elif 'open udemy' in query:
            webbrowser.open("https://www.udemy.com")
        elif 'open ssuet' in query:
            webbrowser.open("https://ssuet.edu.pk")
        elif 'open github' in query:
            webbrowser.open("https://github.com")
        elif 'play music' in query or 'play some music' in query:
            speak("Playing random music")
            playRandomMusic()
        elif 'the time' in query:
            strTime = datetime.datetime.now().strftime("%H:%M:%S")
            speak(f"Sir, the time is {strTime}")
        elif 'stop' in query:
            speak("Goodbye sir, have a nice day!")
            self.close()
        elif 'open code' in query:
            codePath = "C:\\Users\\USER\\AppData\\Roaming\\Microsoft\\Windows\\Start Menu\\Programs\\Visual Studio Code"
            os.startfile(codePath)  
        elif 'email to abdul' in query:
            try:
                speak("What should I say?")
                content = takeCommand()
                to = "ghaniimam5@gmail.com"
                sendEmail(to, content)
            except Exception as e:
                print(e)
                speak("Sorry my friend abdulghani bhai. I am not able to send this email")
        elif 'translate' in query:
            try:
                speak("What text do you want to translate?")
                text_to_translate = takeCommand()
                speak("Which language do you want to translate to?")
                language = takeCommand()
                dest_language = getLanguageCode(language)
                translated_text = translateText(text_to_translate, dest_language)
                print(f"Translated Text: {translated_text}")
                speak(f"The translated text is: {translated_text}")
            except Exception as e:
                print(e)
                speak("Sorry, I could not translate the text")
        elif 'weather in' in query:
            city = query.split("in")[-1].strip()
            weather_info = getWeather(city)
            speak(f"The weather in {city} is {weather_info}")
        elif 'tell me a joke' in query:
            joke = pyjokes.get_joke()
            print(joke)
            speak(joke)

if __name__ == "__main__":
    app = QApplication(sys.argv)
    gui = VirtualAssistantGUI()
    gui.show()
    sys.exit(app.exec_())

import sys
import webbrowser
import pyttsx3
import pyjokes
import datetime
import speech_recognition as sr
import wikipedia
import random
import os
import smtplib
from googletrans import Translator
import requests
from bs4 import BeautifulSoup
from PyQt5.QtWidgets import QApplication, QMainWindow, QPushButton, QLabel
from PyQt5.QtGui import QPixmap
from PyQt5.QtCore import Qt
from PIL import Image
class AssistantGUI(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Assistant")
        self.setGeometry(100, 100, 800, 600)

        # Set background image
        self.set_background_image("assistant.jpg")

        # Add buttons
        self.add_buttons()

        # Initialize speech recognition
        self.recognizer = sr.Recognizer()
        self.microphone = sr.Microphone()

        # Greet the user
        self.speak_message()

    def speak_message(self):
        speak("Hello Abdul Ghani sir. How may I help you?")


    # Other methods remain the same


# Initialize the pyttsx3 engine
engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[0].id)

def speak(audio):
    engine.say(audio)
    engine.runAndWait()

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

def getJoke():
    joke = pyjokes.get_joke()
    print(joke)
    speak(joke)

def getCurrentTime():
    strTime = datetime.datetime.now().strftime("%H:%M:%S")
    speak(f"Sir, the time is {strTime}")

class AssistantGUI(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Assistant")
        self.setGeometry(100, 100, 800, 600)

        # Set background image
        self.set_background_image("assistant.jpg")

        # Add buttons
        self.add_buttons()

        # Initialize speech recognition
        self.recognizer = sr.Recognizer()
        self.microphone = sr.Microphone()

    def set_background_image(self, image_path):
        background_label = QLabel(self)
        pixmap = QPixmap(image_path)
        background_label.setPixmap(pixmap.scaled(self.size()))
        background_label.setAlignment(Qt.AlignCenter)
        background_label.setGeometry(0, 0, self.width(), self.height())
    def open_google(self):
        webbrowser.open("https://www.google.com")    

    def add_buttons(self):
        
        # Speak button
        self.button_speak = QPushButton("Speak", self)
        self.button_speak.setGeometry(50, 50, 100, 30)
        self.button_speak.clicked.connect(self.listen_and_execute)
        
        # Wikipedia button
        self.button_wiki = QPushButton("Wikipedia", self)
        self.button_wiki.setGeometry(50, 100, 100, 30)
        self.button_wiki.clicked.connect(self.search_wikipedia)




        # Date button
        self.button_date = QPushButton("Show Date", self)
        self.button_date.setGeometry(50, 250, 150, 30)
        self.button_date.clicked.connect(self.show_date)




        # Open YouTube button
        self.button_youtube = QPushButton("Open YouTube", self)
        self.button_youtube.setGeometry(50, 150, 100, 30)
        self.button_youtube.clicked.connect(self.open_youtube)





        # Google button
        self.button_google = QPushButton("Open Google", self)
        self.button_google.setGeometry(200, 50, 150, 30)
        self.button_google.clicked.connect(self.open_google)




        # Wikipedia button
        self.button_wikipedia = QPushButton("Search Wikipedia", self)
        self.button_wikipedia.setGeometry(200, 150, 150, 30)
        self.button_wikipedia.clicked.connect(self.search_wikipedia)


        

        

        # Tell Joke button
        self.button_joke = QPushButton("Tell Joke", self)
        self.button_joke.setGeometry(50, 300, 100, 30)
        self.button_joke.clicked.connect(self.tell_joke)

        # Get Current Time button
        self.button_time = QPushButton("Current Time", self)
        self.button_time.setGeometry(50, 350, 100, 30)
        self.button_time.clicked.connect(self.get_current_time)



        #weather
        self.button_weather = QPushButton("Weather", self)
        self.button_weather.setGeometry(50, 400, 100, 30)
        self.button_weather.clicked.connect(self.get_weather)





        # VS Code button
        self.button_vscode = QPushButton("Open VS Code", self)
        self.button_vscode.setGeometry(50, 200, 150, 30)
        self.button_vscode.clicked.connect(self.open_vscode)

        


        # Email button
        self.button_email = QPushButton("Send Email", self)
        self.button_email.setGeometry(50, 250, 100, 30)
        self.button_email.clicked.connect(self.send_email)



        # Play Music button
        self.button_music = QPushButton("Play Music", self)
        self.button_music.setGeometry(50, 200, 100, 30)
        self.button_music.clicked.connect(self.play_random_music)
        



    # Speak button
   
    def listen_and_execute(self):
        with self.microphone as source:
                print("Listening...")
                self.recognizer.adjust_for_ambient_noise(source)
                audio = self.recognizer.listen(source)

        try:
            print("Recognizing...")
            query = self.recognizer.recognize_google(audio, language='en-in')
            print(f"User said: {query}")
            self.execute_command(query.lower())
        except sr.UnknownValueError:
            print("Could not understand audio")
        except sr.RequestError as e:
            print(f"Could not request results; {e}")

    def execute_command(self, query):
        if 'wikipedia' in query:
            self.search_wikipedia()
        elif 'open youtube' in query:
            self.open_youtube()
        elif 'play music' in query:
            self.play_random_music()
        elif 'send email' in query:

            self.send_email()
        elif 'tell joke' in query:
            self.tell_joke()
        elif 'current time' in query:
            self.get_current_time()

    def search_wikipedia(self):
        speak("What do you want to search on Wikipedia?")
        query = takeCommand()
        try:
            results = wikipedia.summary(query, sentences=2)
            speak("According to Wikipedia")
            speak(results)
        except wikipedia.exceptions.PageError:
            speak("Sorry, I couldn't find any information on Wikipedia.")
        except wikipedia.exceptions.DisambiguationError:
            speak("There are multiple matches for your query. Please be more specific.")
        except Exception as e:
            print(e)
            speak("Sorry, I encountered an error while searching Wikipedia.")
   
        

    def open_youtube(self):
        webbrowser.open("https://www.youtube.com")

    def play_random_music(self):
        speak("Playing random music")
        playRandomMusic()
    def open_vscode(self):
        os.system("code")    

    def send_email(self):
        try:
            speak("What should I say?")
            content = takeCommand()
            to = "ghaniimam5@gmail.com"
            sendEmail(to, content)
        except Exception as e:
            print(e)
            speak("Sorry, I am not able to send this email")

    def tell_joke(self):
        getJoke()
    def show_date(self):
        current_date = datetime.datetime.now().strftime("%B %d, %Y")
        speak(f"Today's date is {current_date}")    

    def get_current_time(self):
        getCurrentTime()
    def get_weather(self):
        speak("Please specify the city for weather information.")
        city = takeCommand()
        weather_info = getWeather(city)
        speak(weather_info)    

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = AssistantGUI()
    window.show()
    sys.exit(app.exec_())

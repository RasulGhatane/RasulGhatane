import speech_recognition as sr
import pyttsx3
import datetime
import wikipedia
import webbrowser
import os
import time
import subprocess
import wolframalpha
import json
import requests


print('Loading your AI personal assistant - Algo')

engine=pyttsx3.init('sapi5')
voices=engine.getProperty('voices')
engine.setProperty('voice','voices[1].id')


def speak(text):
    engine.say(text)
    engine.runAndWait()

def wishMe():
    hour=datetime.datetime.now().hour
    if hour>=0 and hour<12:
        speak("Hello,Good Morning")
        print("Hello,Good Morning")
    elif hour>=12 and hour<18:
        speak("Hello,Good Afternoon")
        print("Hello,Good Afternoon")
    else:
        speak("Hello,Good Evening")
        print("Hello,Good Evening")

def takeCommand():
    r=sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        audio=r.listen(source)

        try:
            statement=r.recognize_google(audio,language='en-in')
            print(f"user said:{statement}\n")

        except Exception as e:
            speak("Pardon me, please say that again")
            return "None"
        return statement

speak("Loading your AI personal assistant Algo")
wishMe()


if __name__=='__main__':


    while True:
        speak("Tell me how can I help you now?")
        statement = takeCommand().lower()
        if statement==0:
            continue

        if "goodbye" in statement or "ok bye" in statement or "stop" in statement:
            speak('your personal assistant Algo is shutting down,Good bye')
            print('your personal assistant Algo is shutting down,Good bye')
            break



        if 'wikipedia' in statement:
            speak('Searching Wikipedia...')
            statement =statement.replace("wikipedia", "")
            results = wikipedia.summary(statement, sentences=3)
            speak("According to Wikipedia")
            print(results)
            speak(results)

        elif 'open youtube' in statement:
            webbrowser.open_new_tab("https://www.youtube.com")
            speak("youtube is open now")
            time.sleep(5)

        elif 'open google' in statement:
            webbrowser.open_new_tab("https://www.google.com")
            speak("Google chrome is open now")
            time.sleep(5)

        elif 'open gmail' in statement:
            webbrowser.open_new_tab("gmail.com")
            speak("Google Mail open now")
            print("Google main open now")
            time.sleep(5)
        
        elif 'open facebook' in statement:
            webbrowser.open_new_tab("https://www.facebook.com")
            speak("Facebook is open now")
            print("Facebook is open now")
            time.sleep(5)

        elif "weather" in statement:
            api_key="8ef61edcf1c576d65d836254e11ea420"
            base_url="https://api.openweathermap.org/data/2.5/weather?"
            speak("whats the city name")
            city_name=takeCommand()
            complete_url=base_url+"appid="+api_key+"&q="+city_name
            response = requests.get(complete_url)
            x=response.json()
            if x["cod"]!="404":
                y=x["main"]
                current_temperature = y["temp"]
                current_humidiy = y["humidity"]
                z = x["weather"]
                weather_description = z[0]["description"]
                speak(" Temperature in kelvin unit is " +
                      str(current_temperature) +
                      "\n humidity in percentage is " +
                      str(current_humidiy) +
                      "\n description  " +
                      str(weather_description))
                print(" Temperature in kelvin unit = " +
                      str(current_temperature) +
                      "\n humidity (in percentage) = " +
                      str(current_humidiy) +
                      "\n description = " +
                      str(weather_description))

            else:
                speak(" City Not Found ")

        elif 'time' in statement:
            strTime=datetime.datetime.now().strftime("%H:%M:%S")
            speak(f"the time is {strTime}")

        elif 'play music' in statement:
            music_dir = 'C:\\Users\\Rasul Ghatane\\Music'
            songs = os.listdir(music_dir)
            print(songs)    
            os.startfile(os.path.join(music_dir, songs[0]))

        elif 'open code' in statement:
            codePath = "C:\\Users\\Rasul Ghatane\\AppData\\Local\\Programs\\Microsoft VS Code\\Code.exe"
            os.startfile(codePath)
            speak("Opening VS code.")

        elif 'open zoom' in statement:
            zoomPath = "C:\\Users\\Rasul Ghatane\\AppData\\Roaming\\Zoom\\bin\\Zoom.exe"
            os.startfile(zoomPath)
            speak("Opening Zoom.")

        elif 'who are you' in statement or 'what can you do' in statement:
            speak('I am Algo version 1 point O your personal assistant. I am programmed to minor tasks like'
                  'opening youtube,google chrome,gmail and stackoverflow ,predict time,search wikipedia,predict weather' 
                  'in different cities , get top headline news from BBC and you can ask me computational or geographical questions too!')


        elif "who made you" in statement or "who created you" in statement or "who discovered you" in statement:
            speak("I was built by Rasul")
            print("I was built by Rasul")

        elif "open stackoverflow" in statement:
            webbrowser.open_new_tab("https://stackoverflow.com/login")
            speak("Here is stackoverflow")
            print("Here is stackoverflow.")

        elif 'news' in statement:
            news = webbrowser.open_new_tab("https://www.bbc.com/news")
            speak('Here are some headlines from the BBC,Happy reading')
            print("Here are some headlines from the BBC,Happy reading.")
            time.sleep(6)
      

        elif 'what is your name' in statement or "what's your name" in statement:
            speak("My name is Algo D. Luffy and I want to become ho-kagay someday.")
            print("My name is Algo D. Luffy and I want to become hokage someday.")

        elif 'do you watch anime' in statement:
            speak("Yes, Naruto is my favorite anime.")
            print("Yes, Naruto is my favorite anime.")

        elif 'sharingan' in statement:
            speak("You're under my genjutsu.")
            print("You're under my genjutsu.")
        
        elif 'i am not feeling good.' in statement or "i am not feeling well" in statement:
            speak("OH! Take care.")
            print("OH! Take care.")

        elif 'search'  in statement:
            statement = statement.replace("search", "")
            webbrowser.open_new_tab(statement)
            time.sleep(5)

        elif 'ask' in statement:
            speak('I can answer to computational and geographical questions and what question do you want to ask now')
            question=takeCommand()
            app_id="GV3P8Y-WG738YLTA4"
            client = wolframalpha.Client('GV3P8Y-WG738YLTA4')
            res = client.query(question)
            answer = next(res.results).text
            speak(answer)
            print(answer)


            
        elif "log off" in statement or "sign out" in statement:
            speak("Ok , your pc will log off in 10 sec make sure you exit from all applications")
            subprocess.call(["shutdown", "/l"])

time.sleep(3)

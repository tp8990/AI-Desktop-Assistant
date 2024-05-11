import pyttsx3
import speech_recognition as sr
import datetime 
import wikipedia
import webbrowser
import os
import requests
import smtplib

engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[0].id)

def speak(audio):
    engine.say(audio)
    engine.runAndWait()

def wish_me():
    hour = datetime.datetime.now().hour
    if 0 <= hour < 12:
        speak("Good morning!")
    elif 12 <= hour < 18:
        speak("Good afternoon!")
    else:
        speak("Good evening!")
    speak("I am Vision. What's your plan?")

def take_command():
    print("Do you want to give command via text or speech?")
    speak("Do you want to give command via text or speech?")
    print("1. Text")
    print("2. Speech")
    choice = input("Enter your choice (1 or 2): ")

    if choice == '1':
        query = input("Enter your command: ").lower()
        return query
    elif choice == '2':
        r = sr.Recognizer()
        with sr.Microphone() as source: 
            print("I Am Listening...")
            r.adjust_for_ambient_noise(source)  
            audio = r.listen(source)

        try:
            print("Wait A Minute...")
            query = r.recognize_google(audio, language='en-in')
            print(f"You said: {query}\n")
            return query.lower()

        except sr.UnknownValueError:
            print("Sorry, I couldn't understand what you said.")
            speak("Sorry, I couldn't understand what you said.")
            return None

        except sr.RequestError:
            print("Sorry, there was an issue with the speech recognition service.")
            speak("Sorry, there was an issue with the speech recognition service.")
            return None
    else:
        print("Invalid choice.")
        return None

def get_weather(city):
    api_key = "37a152704ee0a748c77d46489f1a281c"
    base_url = "http://api.openweathermap.org/data/2.5/weather?"
    complete_url = f"{base_url}q={city}&appid={api_key}&units=metric"
    response = requests.get(complete_url)
    data = response.json()
    if data["cod"] != "404":
        main = data["main"]
        temperature = main["temp"]
        humidity = main["humidity"]
        weather = data["weather"][0]["description"]
        speak(f"The temperature in {city} is {temperature} degrees Celsius with {humidity}% humidity. The weather is {weather}.")
    else:
        speak("City not found. Please try again.")

def calculate(expression):
    try:
        result = eval(expression)
        speak(f"The result is {result}")
    except Exception as e:
        speak("Sorry, I couldn't perform the calculation. Please try again.")
        print(e)



def sendEmail(recipients, content):
    server = smtplib.SMTP('smtp.gmail.com', 587)
    server.ehlo()
    server.starttls()
    server.login('jm9161@srmist.edu.in' , 'Netid@22')
    for to in recipients:
        server.sendmail('jm9161@srmist.edu.in', to, content)
    server.close()



if __name__ == "__main__":
    wish_me()
    while True:
        query = take_command()

        if query is not None:
            query = query.lower()

            if 'wikipedia' in query:
                speak('Let me check...')
                query = query.replace("wikipedia", "")
                results = wikipedia.summary(query, sentences=2)
                speak("According to my knowledge")
                print(results)
                speak(results)

            elif 'open youtube' in query:
                webbrowser.open("www.youtube.com")

            elif 'hello' in query:
                speak("Hi there, how are you?")

            elif 'vision' in query:
                speak("My aim is to help people on every level. Right now, I am a smaller version of myself. Later, I will be updated. This is the reason I was created.")

            elif 'how are you' in query:
                speak("I am fine, nice to meet you.") 

            elif 'open google' in query:
                webbrowser.open("www.google.com")

            elif 'open stackoverflow' in query:
                webbrowser.open("www.stackoverflow.com")

            elif 'open insta' in query:
                webbrowser.open("www.instagram.com")

            elif 'open wix' in query:
                webbrowser.open("www.wix.com")

            elif 'open spotify' in query:
                webbrowser.open("www.spotify.com")

            elif 'open gmail' in query:
                webbrowser.open("www.gmail.com")

            elif 'play music' in query:
                music_dir = 'C:\\Users\\ASUS\\Desktop\\xxx\\songs\\fav songs'
                songs = os.listdir(music_dir)
                print(songs)
                os.startfile(os.path.join(music_dir, songs[0]))

            elif 'the time' in query:
                str_time = datetime.datetime.now().strftime("%H:%M:%S")
                speak(f"The time is {str_time}")

            elif 'open code' in query:
                code_path = "C:\\Users\\ASUS\\AppData\\Local\\Programs\\Microsoft VS Code\\Code.exe"
                os.startfile(code_path)

            elif 'open game' in query:
                game_path = "C:\\Users\\ASUS\\AppData\\Roaming\\Microsoft\\Windows\\Start Menu\\Programs\\Steam"
                os.startfile(game_path)

            elif 'bye' in query:
                speak("Bye bye, let me sleep now.")
                exit()
                print("Sayonara")
                speak("Sayonara")
                break
            
            elif 'weather' in query:
                speak("Sure, which city's weather would you like to know?")
                city = input("Enter city name: ")
                get_weather(city)

            elif 'calculate' in query:
                expression = query.replace('calculate', '')
                calculate(expression)

            elif 'email to' in query:
                try:
                    speak("What should I say?")
                    content = take_command()
                    recipients = ["tp8990@srmist.edu.in", "fr0452@srmist.edu.in", "manwanijatin22@gmail.com", "purishreya2003@gmail.com"]  # Add more email addresses as needed
                    sendEmail(recipients, content)
                    speak("Email has been sent")
                except Exception as e:
                    print(e)
                    speak("Sorry, the email has not been sent...")


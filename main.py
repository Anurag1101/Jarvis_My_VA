import speech_recognition as sr
import webbrowser
import pyttsx3
import musicLibrary
import requests
import datetime
# import os

#pip install pocketsphinx

recognizer = sr.Recognizer()
engine = pyttsx3.init() 
# newsapi = "Your News API"

def speak(text):
    engine.say(text)
    engine.runAndWait()
    
def wishMe():
    hour = int(datetime.datetime.now().hour)
    if hour>=0 and hour<12:
        speak("Good Morning!")

    elif hour>=12 and hour<17:
        speak("Good Afternoon!")   

    else:
        speak("Good Evening!")
        
def tellTime():
    current_time = datetime.datetime.now().strftime("%I:%M %p")
    speak(f"The time is {current_time}")

def processCommand(c):
    if "open google" in c.lower():
        webbrowser.open("https://google.com")
    elif "open facebook" in c.lower():
        webbrowser.open("https://facebook.com")
    elif "open youtube" in c.lower():
        webbrowser.open("https://youtube.com")
    elif "open linkedin" in c.lower():
        webbrowser.open("https://linkedin.com")
    elif "open chat" in c.lower():
        webbrowser.open("https://chatgpt.com")
    elif "open netflix" in c.lower():
        webbrowser.open("https://netflix.com")
    elif "the time" in c.lower():
        tellTime()
    elif c.lower().startswith("play"):
        song = c.lower().split(" ")[1]
        link = musicLibrary.music[song]
        webbrowser.open(link)
        
    elif "news" in c.lower():
        r = requests.get(f"https://newsapi.org/v2/top-headlines?country=in&apiKey={newsapi}")
        if r.status_code == 200:
            # Parse the JSON response
            data = r.json()
            
            # Extract the articles
            articles = data.get('articles', [])
            
            # Print the headlines
            for article in articles:
                speak(article['title'])
    
    # for news simply say play news if api is exhausted.

if __name__ == "__main__":
    speak("Initializing Jarvis....")
    wishMe()
    speak("I am Jarvis Sir. Please tell me how may I help you")
    
    
    with sr.Microphone() as source:
        while True:
            print("recognizing...")
            try:
                
                recognizer.adjust_for_ambient_noise(source, duration=1)
                recognizer.dynamic_energy_threshold = True
                recognizer.energy_threshold = 1200  

                audio = recognizer.listen(source, timeout=5, phrase_time_limit=5) 
                word = recognizer.recognize_google(audio)
                
                if word.lower() == "jarvis":
                    speak("Yes")
                    print("Jarvis Active...")
                    
                    audio = recognizer.listen(source,timeout=5, phrase_time_limit=5)
                    recognizer.dynamic_energy_threshold = True
                    recognizer.energy_threshold = 1200  
                    command = recognizer.recognize_google(audio)
                    processCommand(command)

            except sr.WaitTimeoutError:
                print("Listening timed out while waiting for phrase to start.")
            except sr.UnknownValueError:
                print("Could not understand audio.")
            except sr.RequestError as e:
                print(f"Could not request results from Google Speech Recognition service; {e}")
            except Exception as e:
                print(f"Error; {e}")

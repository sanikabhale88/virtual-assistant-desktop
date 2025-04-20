import pyttsx3
import speech_recognition as sr
import datetime
import wikipedia
import webbrowser
import os

engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[1].id)

def speak(audio):
    """Convert text to speech."""
    engine.say(audio)
    engine.runAndWait()

def wishMe():
    """Greet the user based on the time of day."""
    hour = int(datetime.datetime.now().hour)
    if hour < 12:
        speak("Good Morning!")
    elif hour < 18:
        speak("Good Afternoon!")
    else:
        speak("Good Evening!")    

    speak("Please tell me how may I help you?")

def takeCommand():
    """Listen for user commands via microphone."""
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        r.pause_threshold = 1
        r.adjust_for_ambient_noise(source)  # Adjust for background noise
        audio = r.listen(source)

    try:
        print("Recognizing...")
        query = r.recognize_google(audio, language='en-in')
        print(f"User said: {query}\n")
        return query.lower()
    except sr.UnknownValueError:
        print("Sorry, I could not understand. Can you repeat?")
        return "None"
    except sr.RequestError:
        print("Could not request results, check your internet connection.")
        return "None"

if __name__ == "__main__":
    wishMe()
    while True:
        query = takeCommand()

        if query == "none":
            continue  # Retry listening

        if 'wikipedia' in query:
            speak('Searching Wikipedia...')
            query = query.replace("wikipedia", "")
            try:
                results = wikipedia.summary(query, sentences=1)
                speak("According to Wikipedia")
                print(results)
                speak(results)
            except wikipedia.exceptions.DisambiguationError as e:
                speak("There are multiple results, please be more specific.")
            except wikipedia.exceptions.PageError:
                speak("Sorry, I couldn't find anything on Wikipedia.")

        elif 'open youtube' in query:
            webbrowser.open("https://youtube.com")
        
        elif 'open google' in query:
            webbrowser.open("https://google.com")

        elif 'open python' in query:
            webbrowser.open("https://www.python.org/")

        elif 'open github' in query:
            webbrowser.open("https://github.com/")

        elif 'the time' in query:
            strTime = datetime.datetime.now().strftime("%H:%M:%S")
            speak(f"Ma'am, the time is {strTime}")

        elif 'open notepad' in query:
            os.system("notepad")

        elif 'exit' in query or 'bye' in query:
            speak("Goodbye, have a great day!")
            break  # Exit loop
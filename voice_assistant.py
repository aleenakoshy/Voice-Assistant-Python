
import pyttsx3
import datetime
import wikipedia
import webbrowser
import pyjokes



def speak(text):
    print(f"Assistant: {text}")
    local_engine = pyttsx3.init()
    local_engine.setProperty('rate', 170)
    local_engine.say(text)
    local_engine.runAndWait()


def wish_user():
    hour = datetime.datetime.now().hour
    if hour < 12:
        greeting = "Good Morning"
    elif hour < 18:
        greeting = "Good Afternoon"
    else:
        greeting = "Good Evening"
    speak(f"{greeting}! I am your Python voice assistant. How can I help you?")

def take_command():
    return input("You: ").strip().lower()

def run_assistant():
    wish_user()
    while True:
        query = take_command()

        if not query:
            speak("Please type a command.")
            continue

        if 'wikipedia' in query:
            speak("Searching Wikipedia")
            topic = query.replace("wikipedia", "").strip()
            try:
                result = wikipedia.summary(topic, sentences=2)
                speak(result)
            except:
                speak("Sorry, I could not find information on that.")

        elif 'open youtube' in query:
            speak("Opening YouTube")
            webbrowser.open("https://www.youtube.com")

        elif 'open google' in query:
            speak("Opening Google")
            webbrowser.open("https://www.google.com")

        elif 'time' in query:
            current_time = datetime.datetime.now().strftime("%H:%M:%S")
            speak(f"The current time is {current_time}")

        elif 'date' in query:
            today = datetime.datetime.now().strftime("%d %B %Y")
            speak(f"Today's date is {today}")

        elif 'joke' in query:
            speak(pyjokes.get_joke())

        elif 'help' in query:
            speak("You can ask me to search Wikipedia, open Google or YouTube, tell the time, date, or a joke.")

        elif 'exit' in query or 'bye' in query:
            speak("Goodbye! Have a great day.")
            break

        else:
            speak("Sorry, I did not understand that command.")

run_assistant()

import speech_recognition as sr
import pyttsx3
import datetime
import pywhatkit
import wikipedia

listener = sr.Recognizer()
Alexa = pyttsx3.init()
voices = Alexa.getProperty('voices')

def talk(text):
    Alexa.say(text)
    Alexa.runAndWait()


def take_command():
    try:
        with sr.Microphone() as source:
            print('Listening...')
            voice = listener.listen(source)
            command = listener.recognize_google(voice)
            if "Alexa" in command:
                print(command)
                command = command.replace('Alexa', '')
            else:
                print("Error. Use Alexa in your command.")

    except:
        pass
    return command

def run_alexa():
    command = take_command()
    if 'time' in command:
        time = datetime.datetime.now().strftime('%I:%M %p')
        print("Now the time is "+time)
        talk("Now the time is"+time)
    
    elif 'play' in command:
        song = command.replace('play', '')
        talk('playing'+song)
        pywhatkit.playonyt(song)

    elif 'details' in command:
        look_for = command.replace('details', '')
        info = wikipedia.summary(look_for, 2)
        print(info)
        talk(info)

run_alexa()

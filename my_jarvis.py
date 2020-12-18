import pyttsx3
import speech_recognition as sr
import datetime
import smtplib
import wikipedia
import webbrowser
import os

engine=pyttsx3.init('sapi5')
voices=engine.getProperty('voices')
engine.setProperty('voice',voices[0].id)

def speak(audio):
    engine.say(audio)
    engine.runAndWait()

def wishMe():
    hour=int(datetime.datetime.now().hour)
    if hour>6 and hour <12:
       speak("Good morning vishaal sir")
    elif hour>=12 and hour <18:
        speak("Good afternoon vishaal sir")
    elif hour>=18 and hour <24:
        speak("Good evening vishaal sir")

    speak(" I'm Chitti the Robot. Speed 1 terahertz, memory 1 zigabyte. how can i help you vishaal sir")



def takeCommand():

    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Jarvis is listening.......")
        r.pause_threshold= 1
        audio = r.listen(source)

    try:
        print("Recognizing.........")
        query=r.recognize_google(audio,language="en-in")
        print(f"User said {query}\n")

    except Exception as e:
        print("sorry did't able to recognize ...say again")
        return "None"
    return query

def sendEmail(to,content):
    server= smtplib.SMTP('smtp.gmail.com',587)
    server.ehlo()
    server.starttls()
    server.login("situkishaadi@gmail.com","sandeepshikha")
    server.sendmail("situkishaadi@gmail.com",to,content)
    server.close()



if __name__ == '__main__':
    wishMe()
    takeCommand()

    while True:

        query = takeCommand().lower()

        if 'wikipedia' in query:
            speak("searching wikipedia")
            takeCommand("what i have to search")
            query=query.replace("wikipedia","")
            results=wikipedia.summary(query,sentences=3)
            print(results)
            speak(results)

        elif "open google" in query:
            webbrowser.open("google.com")

        elif "open youtube" in query:
            webbrowser.open("youtube.com")

        elif "play music"in query:
            music_dir="'D:\musiC'"
            songs=os.listdir(music_dir)
            print(songs)
            os.startfile(os.path.join(music_dir,songs[0]))


        elif"send email" in query:

           try:
              speak("what should i say")
              content =takeCommand()
              to="vishalkumar15337@gmail.com"
              sendEmail(to,content)
              print("Email has been sent")

           except Exception as e:
              print("Sorry vishaal bhai i am not able to send mail")


        elif "bye" in query:
            speak("good bye vishal sir")
            exit()



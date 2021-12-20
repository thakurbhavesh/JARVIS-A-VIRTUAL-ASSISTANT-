import pyttsx3
import datetime
import speech_recognition as sr
import wikipedia
import webbrowser
import os
import random
import smtplib
import socket 
import calendar
import subprocess
from PIL import Image
from datetime import date

import pyttsx3

import tkinter

import json

import random

import operator

import speech_recognition as sr

import datetime

import wikipedia

import webbrowser

import os

import winshell

import pyjokes



import smtplib

import ctypes

import time

import requests

import shutil
from urllib.request import urlopen

engine=pyttsx3.init('sapi5')
voices=engine.getProperty('voices')
# print(voices[1].id)
engine.setProperty('voice',voices[1].id)

def speak(audio):
    engine.say(audio)
    engine.runAndWait()

def wishMe():
    hour=int(datetime.datetime.now().hour)
    if hour>=0 and hour<12:
        
        speak("Good Morning  Sir ")
    elif hour>=12 and hour<18:
        speak("Good Afternoon Sir")
    else:
        speak("Good Evening Sir")
    assname =("I am your Assistant Shiva")
    speak("How can i Help you, Sir")
    

    speak(assname)
   
def usrname():
    
    speak("What should i call you sir")

    uname = takeCommand()

    speak("Welcome Engineer")

    speak(uname)

    columns = shutil.get_terminal_size().columns

     

    print("#####################".center(columns))

    print("Welcome Mr.", uname.center(columns))

    

     

   

def takeCommand():

      #it takes microphone input and return output      
    r=sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening......")
        r.pause_threshold = 1
        audio=r.listen(source)
    
    try:
        print("Reconizing...")
        query=r.recognize_google(audio)
        print(f"User Said:{query}\n ")

    except Exception as e:
        print(e)

        print("Say that again please......")
        return "bhavesh singh"
    return query

def sendEmail(to,content):
    server=smtplib.SMTP('smtp.gmail.com',587)
    server.ehlo()
    server.starttls()
    server.login('designerweb211@gmail.com','@########')
    server.sendmail('designerweb211@gmail.com',to,content)
    server.close()


if __name__=="__main__":
    usrname()
    wishMe()
    if 1:
        query=takeCommand().lower()
    
    
        if 'wikipedia' in query:
            speak('Searching Wikipedia')
            query=query.replace("wikipedia","")
            results=wikipedia.summary(query,sentences=4)
            result=wikipedia.summary(query,sentences=200)
            speak("According to wikipedia")
            print(result)
            speak(results)
        
        elif 'open youtube' in query:
           speak("opening youtube")
           webbrowser.open("youtube.com")
           
        elif 'score' in query:
           speak("opening score")
           webbrowser.open("cricbuzz.com")
           
        elif 'open google' in query:
           speak("opening google please wait")
           webbrowser.open("google.com")
        
        elif 'play music' in query:
            music_dir='B:\\Non Critical\\songs\\Fav'        
            songs=os.listdir(music_dir)
            #print(songs)
            #a=random.randomint(0,50)
            os.startfile(os.path.join(music_dir,songs[0]))

        elif "weather" in query:
             speak("searching weather")
             webbrowser.open('https://www.accuweather.com/')
        
        elif "job" in query:
            speak("waiting for searching  job")
            webbrowser.open('sarkariresult.com')
            
        elif 'time' in query:
            strTime=datetime.datetime.now().strftime("%H:%M:%S")
            speak(strTime)
            print(strTime)
            
        elif 'code' in query:
            speak("opening visual code")
            codepath="C:\\Users\\Bhavesh Singh\\AppData\\Local\\Programs\\Microsoft VS Code\\Code.exe"
            os.startfile(codepath)
            
        elif 'email' in query:
            try:
               speak("What should i say")
               content=takeCommand()
               to="singhbhavesh682@gmail.com"
               sendEmail(to,content)
               speak("Email Sucessfully Send")
            except Exception as e:
               print(e)
               speak("Sending Failed")


        elif "open geeksforgeeks" in query: 
            speak("Opening GeeksforGeeks ")      # in the open method we just to give the link 
            # of the website and it automatically open  
            # it in your default browser 
              
       
            webbrowser.open("www.geeksforgeeks.com") 

        elif 'open stackoverflow' in query:

            speak("Here you go to Stack Over flow.Happy coding")

            webbrowser.open("stackoverflow.com")   
 

        elif "your  name" in query: 
            speak("I am Shiva. Your personal Assistant")

        elif "calendar" in query:
            yy=2021
            px=calendar.calendar(yy)
            print(px)
           # speak(px)
          
            
        elif 'how are you' in query:

            speak("I am fine, Thank you")

            speak("How are you, Sir")
 

        
        elif 'fine' in query or "good" in query:

            speak("It's good to know that your fine")
 

        elif "change my name to" in query:

            query = query.replace("change my name to", "")

            assname = query
 

        elif "change name" in query:

            speak("What would you like to call me, Sir ")

            assname = takeCommand()

            speak("Thanks for naming me")
 

        elif "what's your name" in query or "What is your name" in query:

            speak("My friends call me")

            speak(assname)

            print("My friends call me", assname)
 

        elif 'exit' in query:

            speak("Thanks for giving me your time")

            exit()
 

        elif "who made you" in query or "who created you" in query: 

            speak("I have been created by bhavesh.")

             

        elif 'joke' in query:

            speak(pyjokes.get_joke())
            print(pyjokes.get_joke())

             

        

        elif 'search' in query or 'play' in query:

             

            query = query.replace("search", "") 

            query = query.replace("play", "")          

            webbrowser.open(query) 
 

        elif "who i am" in query:

            speak("If you talk then definately your human.")
 

        elif "why you came to world" in query:

            speak("Thanks to bhavesh. further It's a secret")
 

       

        elif 'is love' in query:

            speak("It is 7th sense that destroy all other senses")
 
        elif 'i love you' in query:
            speak("i am a machine not a human,but i understand your feeling❤")
        
      


        elif "who are you" in query:

            speak("I am your virtual assistant created by bhavesh")
 

        elif 'reason for you' in query:

            speak("I was created as a Minor project by Mister bhavesh ")
 

        elif 'change background' in query:

            ctypes.windll.user32.SystemParametersInfoW(20, 

                                                       0, 

                                                       "A:\WALLPAPER\Flower",

                                                       0)

            speak("Background changed succesfully")
 

        
 

        elif 'news' in query:

              webbrowser.open('aajtak.in')

              speak('here are some top news from the aaj tak')

        elif 'lock window' in query:

                speak("locking the device")

                ctypes.windll.user32.LockWorkStation()
 

        elif 'shutdown system' in query:

                speak("Hold On a Sec ! Your system is on its way to shut down")

                subprocess.call('shutdown / p /f')

                 

        elif 'empty recycle bin' in query:

            winshell.recycle_bin().empty(confirm = False, show_progress = False, sound = True)

            speak("Recycle Bin Recycled")
 

        elif "don't listen" in query or "stop listening" in query:

            speak("for how much time you want to stop jarvis from listening commands")

            a = int(takeCommand())

            time.sleep(a)

            print(a)
 

        elif "where is" in query:

            query = query.replace("where is", "")

            location = query

            speak("User asked to Locate")

            speak(location)

            webbrowser.open("https://www.google.nl / maps / place/" + location + "")
 

       
 

        elif "restart" in query:

            subprocess.call(["shutdown", "/r"])

             

        elif "hibernate" in query or "sleep" in query:

            speak("Hibernating")

            subprocess.call("shutdown / h")
 

        elif "log off" in query or "sign out" in query:

            speak("Make sure all the application are closed before sign-out")

            time.sleep(5)

            subprocess.call(["shutdown", "/l"])
 

        elif "write a note"  or 'note' in query:

            speak("What should i write, sir")

            note = takeCommand()

            file = open('jarvis.txt', 'w')

            speak("Sir, Should i include date and time")

            snfm = takeCommand()

            if 'yes' in snfm or 'sure' in snfm:
                today = date.today()
                d1 = today.strftime("%d/%m/%Y")
                print("d1 =", d1)


# dd/mm/YY



               

                file.write(d1)

                file.write(" :- ")

                file.write(note)

            else:

                file.write(note)

         

        elif "show note" in query:

            speak("Showing Notes")

            file = open("jarvis.txt", "r") 
 
            print(file.read())

            speak(file.read(6))
 
        

        elif 'python' in query:
            webbrowser.open('python.org')
           
    
         
 
  





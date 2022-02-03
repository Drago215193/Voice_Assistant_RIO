import code
from email.mime import audio
from msilib.schema import AppSearch
import sys
from pyaudio import paInt16
from tkinter import *
from tkinter import messagebox as mb
import pyttsx3
import random
import datetime
import speech_recognition as sr
import wikipedia
import webbrowser
import os
import smtplib
import subprocess
from requests import get
import requests
import json
import wolframalpha
from geopy.geocoders import Nominatim
import cv2
import pyscreenshot
import screen_brightness_control as sbc
import pyautogui
from bs4 import BeautifulSoup
from ecapture import ecapture as ec
import pywhatkit
from gtts import gTTS
from tkinter import *
from PIL import ImageTk,Image

engine = pyttsx3.init('sapi5')
voices =engine.getProperty('voices') 
# print(voices[2])
engine.setProperty('voice', voices[1].id)


def speak(audio):
    engine.say(audio)
    engine.runAndWait()
    
def wishMe():
    hour = int(datetime.datetime.now().hour)
    if hour>=0 and hour<12:
        speak("good Morning")

    elif hour>=12 and hour<18:
        speak("Good Afternoon ")

    else:
        speak("Good Evening")

    speak("I am Rio, sir How may I help you! ") 


def takeCommand():
    #it takes microphonic input from the user and return string output
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening .....")
        r.pause_threshold = 1 
        audio =r.listen(source)


    try:
        print("Recognizing .....")
        query =r.recognize_google(audio,language ='en-in')
        print(f"User said : {query}\n")

    
    except Exception as e:
       # print(e)
        print("Say that again please .....")
        return "None"
    return query

def sendEmail(to,content):
    server = smtplib.SMTP('smtp.gmail.com', 587)
    server.ehlo()
    server.starttls()
    server.login('rioai18092021', 'rio18092021ai')
    server.sendmail('rioai18092021', to , content)
    server.close()


def Task():

  wishMe()
  
  while True :

      query = takeCommand().lower()
      
      if 'your name' in query:
          name=('Sir, My name is Rio')
          print(name)  
          speak(name)  

      elif 'you do' in query or 'help me' in query or 'your job' in query:
          you_do= ("Sir, my job is to answer your queries")
          speak(you_do)
          print(you_do)

      elif 'wikipedia' in query:
          speak('Searching Wikipedia..........')
          query = query.replace("wikipedia" ,"")
          results = wikipedia.summary(query,sentences=2)
          speak("According to Wikipedia")
          print(results)
          speak(results)
 
      elif 'open youtube' in query:
          webbrowser.open("youtube.com")

      elif 'open google' in query:
          speak("Sir, What should i search on Google")
          cm=takeCommand().lower()
          print(cm)
          webbrowser.open(f"{cm}")

      elif 'open stackoverflow' in query:
          webbrowser.open("stackoverflow.com")

      elif 'you like' in query or 'your hobbies' in query:
          like=('Sir I like My creators, and as a hobby i like to do your help')
          print(like)
          speak(like)


      elif 'play music' in query or 'play song' in query or 'play a song' in query:
          music_dir = 'D:\\RIO\\songs'
          songs = os.listdir(music_dir)
          print(songs)
          os.startfile(os.path.join(music_dir, songs[0]))

      elif 'the time' in query:
          strTime =datetime.datetime.now().strftime("%H:%M:%S")
          print (strTime)
          speak(f"Sir, the time is  {strTime}")
      
      elif 'open code' in query:
          codepath= "C:\\Users\\PC-ASUS\\AppData\\Local\\Programs\\Microsoft VS Code\\Code.exe"
          os.startfile(codepath)

      elif 'send email' in query:
          try:
              speak("what should I say?")
              content =takeCommand()
              to = "ankity215193@gmail.com"
              sendEmail(to, content)
              speak("Email has been sent!")
          except Exception as e:
              print(e)
              speak("Soory, I can't send this email at the moment...!")


      elif "ip address"  in query:
             ip=get("http://api.ipify.org").text
             print(f"your IP address is {ip}")
             speak(f"your IP address is{ip}")

    #   elif "whatsapp message" in query:
    #       try:
    #           speak("To Whom")
    #           num=int(input(("To Whom(Phone Number Including +91)---)"))
    #           speak("what should I say?")
    #           msg =takeCommand()
    #           speak("at which hour")
    #           h=int(input("Enter Hour---"))
    #           print(h)
    #           speak("at what minute")
    #           m=int(input("Enter Minute---"))
    #           print(m)
    #           pywhatkit.sendwhatmsg(num,msg,h,m)
    #           speak("Message has been sent!")
    #       except Exception as e:
    #           print(e)
    #           speak("Soory, I can't send this message at the moment...!")


      elif "weather" in query:
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
              speak("Sorry Sir, City Not Found ")

      elif 'where' in query and 'i' in query or 'location' in query:
          try:
                
              geoLoc = Nominatim(user_agent="GetLoc")
            # passing the coordinates
              locname = geoLoc.reverse("21.1845 , 81.3521")
            # printing the address/location name
              out='You Location Is Near To ' + locname.address
              print(out)
              speak(out)
          except:
              out='I Was Unable To Track Your Location'
              print(out)
              speak(out)

      elif 'video' in query and 'youtube' in query:
          query2="What do you want to play in Youtube"
          print(query2)
          speak(query2)

          query=takeCommand()
          
          if (query != ""):
              try:
                  pywhatkit.playonyt(query)
                  print("Playing...")
                  speak("Playing...")

              except:
                  print("Network Error Occured")
                  speak("Network Error Occured")
     
      elif "search in google" in query or "search on google" in query:
          print("What should i search on google")
          speak("What should i search on google")

          cm=takeCommand()
          webbrowser.open(f"{cm}")

#---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------#

      elif 'ask' in query:
          speak('I can answer to computational and geographical questions  and what question do you want to ask now')
          question=takeCommand()
          app_id="Paste your unique ID here "
          client = wolframalpha.Client('R2K75H-7ELALHR35X')
          res = client.query(question)
          answer = next(res.results).text
          speak(answer)
          print(answer)

      elif 'drive' in query:
          query2 =("Which drive you have to open ? C , D : \n")
          print(query2)
          speak(query2)
          query= takeCommand()
          if 'c' in query:
              codepath= "C:"
              os.startfile(codepath)
          elif 'd' in query:
              codepath= "D:"
              os.startfile(codepath)
          else:
              print("No, Such directory found")
              speak("No, Such directory found")
        
      elif 'explorer' in query:
          subprocess.run(["explorer", ","])
  
    #   elif 'video recorder' in query or "mirror" in query or "camera preview":
    #       cap = cv2.VideoCapture(0)
    #       if not cap.isOpened():
    #         raise IOError("Cannot open webcam")
    #       while True:
    #         ret, frame = cap.read()
    #         frame = cv2.resize(frame, None, fx=0.5, fy=0.5, interpolation=cv2.INTER_AREA)
    #         cv2.imshow('Input', frame)
    #         c = cv2.waitKey(1)
    #         if c == 27:
    #             break

    #       cap.release()
    #       cv2.destroyAllWindows()

      elif 'downloads' in query or 'download' in query:
          codepath= "C:\\Users\\PC-ASUS\\Downloads\\"
          os.startfile(codepath)          
    
      elif 'camera' in query:
          codepath = "C:\\Program Files\\WindowsApps\\Microsoft.WindowsCamera_2022.2110.0.0_x64__8wekyb3d8bbwe\\WindowsCamera.exe"
          os.startfile(codepath)

      elif 'calculator' in query:
          codepath= 'C:\\Program Files\\WindowsApps\\Microsoft.WindowsCalculator_11.2112.3.0_x64__8wekyb3d8bbwe\\CalculatorApp.exe'
          os.startfile(codepath)     

      elif 'paint' in query:
          codepath= 'C:\\Program Files\\WindowsApps\\Microsoft.Paint_11.2110.0.0_x64__8wekyb3d8bbwe\\PaintApp\\mspaint.exe'
          os.startfile(codepath)     

      elif 'chrome' in query:
          codepath= 'C:\\Program Files\\Google\Chrome\\Application\\chrome.exe'
          os.startfile(codepath)     
        
      elif 'setting' in query or 'settings' in query:
          codepath= "C:\\Users\\PC-ASUS\\Desktop\\settings.url"
          os.startfile(codepath)          

      elif 'whatsapp' in query:
          codepath= "C:\\Users\\PC-ASUS\\AppData\\Local\\WhatsApp\\WhatsApp.exe"
          os.startfile(codepath)

      elif 'game' in query:
          codepath= "D:\\nfs\\Need For Speed Most Wanted Remaster Edition\\speed.exe"
          os.startfile(codepath)

      elif 'pictures' in query:
          codepath= "C:\\Users\\PC-ASUS\\Pictures\\"
          os.startfile(codepath)

      elif 'task manager' in query or 'taskmanager' in query:
          codepath= "C:\\WINDOWS\\system32\\Taskmgr.exe"
          os.startfile(codepath)

      elif 'notepad' in query:
          codepath= "C:\\Windows\\notepad.exe"
          os.startfile(codepath)

      elif 'github' in query or 'git hub' in query:
          codepath= "C:\\Users\\PC-ASUS\\AppData\\Local\\GitHubDesktop\\GitHubDesktop.exe"
          os.startfile(codepath)
      
      elif "ms office" in query:
          query2="Which office application"
          print(input)
          speak(input)
          query=takeCommand()
          if 'powerpoint' in query or 'power point' in query:
              codepath= 'C:\\Program Files\\Microsoft Office\\root\\Office16\\POWERPNT.exe'
              os.startfile(codepath)

          elif 'excel' in query:
              codepath= 'C:\\Program Files\\Microsoft Office\\root\\Office16\\EXCEL'
              os.startfile(codepath)
        
          elif 'word' in query:
              codepath= 'C:\\Program Files\\Microsoft Office\\root\\Office16\\WINWORD'
              os.startfile(codepath)

          elif 'onenote' in query or 'one note' in query:
              codepath= 'C:\\Program Files\\Microsoft Office\\root\\Office16\\ONENOTE'
              os.startfile(codepath)

          elif "one drive" or 'onedrive':
              codepath="C:\\Program Files\\Microsoft OneDrive\\OneDrive"
              os.startfile(codepath)

          else:
              print("Sorry, I didn't understand.")
              speak("Sorry, I didn't understand.")

#----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------#

    #   elif 'exit' in query:                                                                                                                                                                                         #|
    #     out = 'Okk I am going, Have a good Day sir'                                                                                                                                                                 #|
    #     print(out)                                                                                                                                                                                                  #|
    #     speak(out)                                                                                                                                                                                                  #|
    #     audio.win.destroy()                                                                                                                                                                                         #|

#----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------#


      elif query == '':        
          out = 'You Said Nothing'
          print(out)
          speak(out) 
        
      elif 'screenshot' in query:
          image = pyscreenshot.grab()
          image.show()
          r=random.randint(1,10000000)
          image.save(r'C:\\Users\\PC-ASUS\\Pictures\\rio screenshot\\'+str(r)+'.png')

      elif 'volume up' in query:
          io=0
          while(io<10):
              pyautogui.press("volumeup")
              io += 1
          print("Volume increased")
          speak("Volume increased")
          io=0

      elif 'volume down' in query:
          io=0
          while(io<10):
              pyautogui.press("volumedown")
              io += 1
          print("Volume decreased")
          speak("Volume decreased")
          io=0

      elif 'mute' in query:
          pyautogui.press("volumemute")
          print("Done")
          speak("Done")

    #   elif 'news' in query:
    #       news = webbrowser.open_new_tab("https://timesofindia.indiatimes.com/home/headlines”)
    #       speak('Here are some headlines from the Times of India,Happy reading')
    #       time.sleep(6)

    #   elif "take a photo" in query:
    #       ec.capture(0,"robo camera","img.jpg")

      elif "increase" in query and 'brightness' in query:
          sbc.set_brightness(100)

      elif "decrease" in query and 'brightness' in query:
          sbc.set_brightness(20)

      elif "exit" in query:
          print("Ok I am going, Have a good Day sir")
          speak("Ok I am going, Have a good Day sir")
          sys.exit()

      elif 'shutdown' in query:
        out='Shutting Down The System'                                                                                   #|
        print(out)                                                                             #|
        speak(out)
        os.system('shutdown -s')

      elif "sign out" in query:
          speak("Ok , your pc will log off in 10 sec make sure you exit from all applications")
          subprocess.call(["shutdown", "/l"])
			
  time.sleep(3)


# C drive 
# D drive
# file explorer
# camera
# chrome
# game
# Setting
# paint 
# Calculator
# MS office
# Pictures
#taskmanager
# Notepad 
# Calendar
# Whatsapp
# Mail check 
#news

# brightness and volume

if __name__ == "__main__" :
      while True:
          Permission = takeCommand()
          if 'wake up' in Permission:
              Task()
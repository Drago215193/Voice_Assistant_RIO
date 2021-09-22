import pyttsx3
import datetime
import speech_recognition as sr
import wikipedia
import webbrowser
import os
import smtplib
from requests import get
import requests
import json

# import pywhatkit

engine = pyttsx3.init('sapi5')
voices =engine.getProperty('voices') 
# print(voices[2])
engine.setProperty('voice', voices[3].id)


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

    speak("I am rio, sir How may I help you! ") 


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


if __name__ == "__main__" :

  wishMe()
  while True :

      query = takeCommand().lower()
      
      if 'wikipedia' in query:
          speak('Searching Wikipedia..........')
          query = query.replace("wikipedia" ,"")
          results = wikipedia.summary(query,sentences=2)
          speak("According to Wikipedia")
          print(results)
          speak(results)

      elif 'your name' in query:
          name=('Sir, My name is Rio')
          print(name)  
          speak(name)  

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

      elif 'you do' in query or 'help me' in query or 'your job' in query:
          you_do= ("Sir, my job is to answer your fucking queries")
          speak(you_do)
          print(you_do)

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
              speak(" City Not Found ")


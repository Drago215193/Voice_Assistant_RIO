


#-------------------------------------------------Importing Modules----------------------------------------------------------------------------------------------------------------------------------------------------#




import code
from email.mime import audio
from msilib.schema import AppSearch
import sys
from time import time
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
import psutil
import speedtest
import pyjokes
from twilio.rest import Client
from gtts import gTTS
from tkinter import *
from PIL import ImageTk,Image




#-------------------------------------------------Assistant Voice------------------------------------------------------------------------------------------------------------------------------------------------------#


engine = pyttsx3.init('sapi5')
voices =engine.getProperty('voices') 
# print(voices[2])
engine.setProperty('voice', voices[1].id)


#-------------------------------------------------Speak Function-------------------------------------------------------------------------------------------------------------------------------------------------------#


def speak(audio):
    engine.say(audio)
    engine.runAndWait()


#-------------------------------------------------GOOD MORNING CONDITION-----------------------------------------------------------------------------------------------------------------------------------------------#


def wishMe():
    hour = int(datetime.datetime.now().hour)
    if hour>=0 and hour<12:
        speak("good Morning")

    elif hour>=12 and hour<18:
        speak("Good Afternoon ")

    else:
        speak("Good Evening")

    print("I am Rio, sir How may I help you! ") 
    speak("I am Rio, sir How may I help you! ") 


#-------------------------------------------------Voice Input Function-------------------------------------------------------------------------------------------------------------------------------------------------#


def takeCommand():
    r = sr.Recognizer()                                                                                                 #|It takes microphonic input from the user and return string output
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


#-------------------------------------------------Send Email Function--------------------------------------------------------------------------------------------------------------------------------------------------#


def sendEmail(to,content):
    server = smtplib.SMTP('smtp.gmail.com', 587)
    server.ehlo()
    server.starttls()
    server.login('rioai18092021', 'rio18092021ai')
    server.sendmail('rioai18092021', to , content)
    server.close()


#-------------------------------------------------News Function--------------------------------------------------------------------------------------------------------------------------------------------------------#


def news():
    main_url="https://newsapi.org/v2/top-headlines?country=us&category=business&apiKey=5cde394eefe244fc9a443ea118d12255"

    main_page = requests.get(main_url).json()
    articles = main_page["articles"]
    head=[]
    day=['first','second','third','fourth','fifth']
    for ar in articles:
        head.append(ar["title"])
    for i in range (len(day)):
        print(f"{day[i]} news is {head[i]}")
        speak(f"{day[i]} news is {head[i]}")


#-------------------------------------------------Main Components Class------------------------------------------------------------------------------------------------------------------------------------------------#


class Widget:
    def __init__(self):


#-------------------------------------------------GUI Code-------------------------------------------------------------------------------------------------------------------------------------------------------------#


        root= Tk()

        root.title('rio')
        root.geometry('1040x600')

        img = ImageTk.PhotoImage(Image.open('D:\\git rio\\Voice_Assistant_RIO\\eve.jpg'))
        panel = Label(root, image=img)
        panel.pack(side='right', fill='both', expand='no')

        userText = StringVar()

        userText.set('Your Virtual Assistant')
        userFrame = LabelFrame(root, text='RIO', font=('Railways', 30, 'bold'))
        userFrame.pack(fill='both', expand='yes')
 
        top= Message(userFrame, textvariable=userText, bg='black', fg='white')
        top.config(font=("Century Gothic", 25, 'bold'))
        top.pack(side='top', fill='both', expand='yes')

        btn = Button(root, text='Run', font=('railways', 15, 'bold'),bg='red', fg='white', command=self.clicked).pack(fill='x', expand='no')
        btn2 = Button(root, text='Close', font=('railways', 15,'bold'), bg='yellow', fg='black', command=root.destroy).pack(fill='x', expand='no')
        root.mainloop()


#-------------------------------------------------OnClick Function-----------------------------------------------------------------------------------------------------------------------------------------------------#


    def clicked(self):

        wishMe()
        
        while True :

            query = takeCommand().lower()


#-------------------------------------------------About----------------------------------------------------------------------------------------------------------------------------------------------------------------#
            

            if 'your name' in query:
                name=('Sir, My name is Rio')
                print(name)  
                speak(name)  

            elif 'you like' in query or 'your hobbies' in query:
                like=('Sir I like My creators, and as a hobby i like to do your help')
                print(like)
                speak(like)

            elif 'you do' in query or 'help me' in query or 'your job' in query:
                you_do= ("Sir, my job is to answer your queries")
                speak(you_do)
                print(you_do)


#-------------------------------------------------Wikipedia------------------------------------------------------------------------------------------------------------------------------------------------------------#

            elif 'wikipedia' in query:
                speak('Searching Wikipedia..........')
                query = query.replace("wikipedia" ,"")
                results = wikipedia.summary(query,sentences=2)
                speak("According to Wikipedia")
                print(results)
                speak(results)

#-------------------------------------------------Open Youtube---------------------------------------------------------------------------------------------------------------------------------------------------------#

            elif 'open youtube' in query:
                webbrowser.open("youtube.com")

#-------------------------------------------------Open Google----------------------------------------------------------------------------------------------------------------------------------------------------------#

            elif 'open google' in query:
                speak("Sir, What should i search on Google")
                cm=takeCommand().lower()
                print(cm)
                webbrowser.open(f"{cm}")

#-------------------------------------------------stackoverflow--------------------------------------------------------------------------------------------------------------------------------------------------------#

            elif 'open stackoverflow' in query:
                webbrowser.open("stackoverflow.com")

#-------------------------------------------------play music-----------------------------------------------------------------------------------------------------------------------------------------------------------#

            elif 'play music' in query or 'play song' in query or 'play a song' in query:
                try:
                    print("Playing Music")
                    speak("Playing Music")
                    music_dir = 'D:\\RIO\\songs'
                    songs = os.listdir(music_dir)
                    r = random.randint(0,len(music_dir) - 1)
                    print(songs)
                    os.startfile(os.path.join(music_dir, songs[r]))

                except:
                    music_dir = 'D:\\RIO\\songs'
                    songs = os.listdir(music_dir)
                    print(songs)
                    os.startfile(os.path.join(music_dir, songs[0]))

#-------------------------------------------------Time-----------------------------------------------------------------------------------------------------------------------------------------------------------------#

            elif 'the time' in query:
                strTime =datetime.datetime.now().strftime("%H:%M:%S")
                print (strTime)
                speak(f"Sir, the time is  {strTime}")

#-------------------------------------------------E-mail Send----------------------------------------------------------------------------------------------------------------------------------------------------------#

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

#-------------------------------------------------IP address-----------------------------------------------------------------------------------------------------------------------------------------------------------#

            elif "ip address"  in query:
                    ip=get("http://api.ipify.org").text
                    print(f"your IP address is {ip}")
                    speak(f"your IP address is{ip}")

#-------------------------------------------------Whastapp Msg---------------------------------------------------------------------------------------------------------------------------------------------------------#

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

#-------------------------------------------------Weather Forecast-----------------------------------------------------------------------------------------------------------------------------------------------------#

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

#-------------------------------------------------Location-------------------------------------------------------------------------------------------------------------------------------------------------------------#

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

#-------------------------------------------------Youtube search-------------------------------------------------------------------------------------------------------------------------------------------------------#

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

#-------------------------------------------------Google Search--------------------------------------------------------------------------------------------------------------------------------------------------------#

            elif "search in google" in query or "search on google" in query:
                print("What should i search on google")
                speak("What should i search on google")

                cm=takeCommand()
                webbrowser.open(f"{cm}")

#-------------------------------------------------Mathematical and Geometrical Questions-------------------------------------------------------------------------------------------------------------------------------#

            elif 'ask' in query or "computational" in query or "geographical" in query:
                speak('I can answer to computational and geographical questions  and what question do you want to ask now')
                question=takeCommand()
                app_id="Paste your unique ID here "
                client = wolframalpha.Client('R2K75H-7ELALHR35X')
                res = client.query(question)
                answer = next(res.results).text
                print(answer)
                speak(answer)


#-------------------------------------------------Local Disk(C,D)------------------------------------------------------------------------------------------------------------------------------------------------------#

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

 #-------------------------------------------------Video Recorder------------------------------------------------------------------------------------------------------------------------------------------------------#

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

#-------------------------------------------------Notepad--------------------------------------------------------------------------------------------------------------------------------------------------------------#

            elif 'open notepad' in query:
                codepath= "C:\\Windows\\notepad.exe"
                os.startfile(codepath)

            elif 'close notepad' in query:
                print("Closing notepad")
                os.system("taskkill /f /im notepad.exe")      

#-------------------------------------------------V S Code-------------------------------------------------------------------------------------------------------------------------------------------------------------#

            elif 'open code editor' in query or "open vs code" in query:
                codepath= "C:\\Users\\PC-ASUS\\AppData\\Local\\Programs\\Microsoft VS Code\\Code.exe"
                os.startfile(codepath)

            elif 'close code editor' in query or "close vs code" in query:
                print("Closing code editor")
                os.system("taskkill /f /im Code.exe")      

#-------------------------------------------------camera---------------------------------------------------------------------------------------------------------------------------------------------------------------#

            elif 'open camera' in query:
                codepath = "C:\\Program Files\\WindowsApps\\Microsoft.WindowsCamera_2022.2110.0.0_x64__8wekyb3d8bbwe\\WindowsCamera.exe"
                os.startfile(codepath)

            elif 'close camera' in query:
                print("Closing camera")
                os.system("taskkill /f /im WindowsCamera.exe")  

#-------------------------------------------------calculator-----------------------------------------------------------------------------------------------------------------------------------------------------------#

            elif 'open calculator' in query:
                codepath= 'C:\\Program Files\\WindowsApps\\Microsoft.WindowsCalculator_11.2112.3.0_x64__8wekyb3d8bbwe\\CalculatorApp.exe'
                os.startfile(codepath)     

            elif 'close calculator' in query:
                print("Closing calculator")
                os.system("taskkill /f /im CalculatorApp.exe") 

#-------------------------------------------------Paint----------------------------------------------------------------------------------------------------------------------------------------------------------------#

            elif 'open paint' in query:
                codepath= 'C:\\Program Files\\WindowsApps\\Microsoft.Paint_11.2110.0.0_x64__8wekyb3d8bbwe\\PaintApp\\mspaint.exe'
                os.startfile(codepath)     

            elif 'close paint' in query:
                print("Closing paint")
                os.system("taskkill /f /im mspaint.exe") 

#-------------------------------------------------Google Chrome--------------------------------------------------------------------------------------------------------------------------------------------------------#
            
            
            elif 'open chrome' in query:
                codepath= 'C:\\Program Files\\Google\Chrome\\Application\\chrome.exe'
                os.startfile(codepath)     

            elif 'close google chrome' in query or 'close chrome' in query:
                print("Closing google chrome")
                os.system("taskkill /f /im chrome.exe")   

#-------------------------------------------------WhatsApp-------------------------------------------------------------------------------------------------------------------------------------------------------------#
       
            elif 'open whatsapp' in query:
                codepath= "C:\\Users\\PC-ASUS\\AppData\\Local\\WhatsApp\\WhatsApp.exe"
                os.startfile(codepath)

            elif 'close whatsapp' in query:
                print("Closing whatsapp")
                os.system("taskkill /f /im WhatsApp.exe") 

#-------------------------------------------------Game-----------------------------------------------------------------------------------------------------------------------------------------------------------------#

            elif 'open game' in query:
                codepath= "D:\\nfs\\Need For Speed Most Wanted Remaster Edition\\speed.exe"
                os.startfile(codepath)

            elif 'close game' in query:
                print("Closing game")
                os.system("taskkill /f /im speed.exe") 

#-------------------------------------------------taskmanager----------------------------------------------------------------------------------------------------------------------------------------------------------#

            elif 'open task manager' in query or 'open taskmanager' in query:
                codepath= "C:\\WINDOWS\\system32\\Taskmgr.exe"
                os.startfile(codepath)

            elif 'close task manager' in query or 'close taskmanager' in query:
                print("Closing taskmanager")
                os.system("taskkill /f /im Taskmgr.exe") 

#-------------------------------------------------github---------------------------------------------------------------------------------------------------------------------------------------------------------------#

            elif 'open github' in query or 'open git hub' in query:
                codepath= "C:\\Users\\PC-ASUS\\AppData\\Local\\GitHubDesktop\\GitHubDesktop.exe"
                os.startfile(codepath)

            elif 'close git hub' in query or 'close github' in query:
                print("Closing github")
                os.system("taskkill /f /im GitHubDesktop.exe") 

#-------------------------------------------------ms office-------------------------------------------------------------------------------------------------------------------------------------------------------------#


            elif "open microsoft office" in query:
                input2="Which office application"
                print(input2)
                speak(input2)
                query2=takeCommand().lower()
                if 'powerpoint' in query2 or 'power point' in query2:
                    codepath= 'C:\\Program Files\\Microsoft Office\\root\\Office16\\POWERPNT.exe'                                   #|  Microsoft Powerpoint Opening
                    os.startfile(codepath)

                elif 'excel' in query2:
                    codepath= 'C:\\Program Files\\Microsoft Office\\root\\Office16\\EXCEL.exe'                                      #|  Microsoft Excel Opening
                    os.startfile(codepath)
                
                elif 'word' in query2:
                    codepath= 'C:\\Program Files\\Microsoft Office\\root\\Office16\\WINWORD.exe'                                    #|  Microsoft Word Opening
                    os.startfile(codepath)

                elif 'onenote' in query2 or 'one note' in query2:
                    codepath= 'C:\\Program Files\\Microsoft Office\\root\\Office16\\ONENOTE.exe'                                    #|  Microsoft OneNote Opening
                    os.startfile(codepath)

                elif "one drive" in query2 or 'onedrive'in query2:
                    codepath="C:\\Program Files\\Microsoft OneDrive\\OneDrive.exe"                                                  #|  Microsoft OneDrive Opening
                    os.startfile(codepath)

                else:
                    print("Sorry, I didn't understand.")
                    speak("Sorry, I didn't understand.")

 #-------------------------------------------------ms office closing---------------------------------------------------------------------------------------------------------------------------------------------------#

            elif 'close power point' in query or 'close powerpoint' in query:                                                       #|  Microsoft Powerpoint Closing
                print("Closing powerpoint")
                os.system("taskkill /f /im POWERPNT.exe") 

            elif 'close excel' in query:                                                                                            #|  Microsoft Excel Closing
                print("Closing excel")  
                os.system("taskkill /f /im EXCEL.exe") 

            elif 'close word' in query:                                                                                             #|  Microsoft Word Closing
                print("Closing word")
                os.system("taskkill /f /im WINWORD.exe") 

            elif 'close onenote' in query or 'close one note' in query:                                                             #|  Microsoft OneNote Closing
                print("Closing onenote")
                os.system("taskkill /f /im ONENOTE.exe") 

            elif 'close onedrive' in query or 'close one drive' in query:                                                           #|  Microsoft OneDrive Closing
                print("Closing onedrive")
                os.system("taskkill /f /im OneDrive.exe") 

#-------------------------------------------------Pictures Folder------------------------------------------------------------------------------------------------------------------------------------------------------#

            elif 'pictures' in query:
                codepath= "C:\\Users\\PC-ASUS\\Pictures\\"
                os.startfile(codepath)

#-------------------------------------------------Settings-------------------------------------------------------------------------------------------------------------------------------------------------------------#

            elif 'open setting' in query or 'open settings' in query:
                codepath= "C:\\Users\\PC-ASUS\\Desktop\\settings.url"
                os.startfile(codepath)   

#-------------------------------------------------File Explorer--------------------------------------------------------------------------------------------------------------------------------------------------------#

            elif 'open explorer' in query:
                subprocess.run(["explorer", ","])

#-------------------------------------------------Downloads Folder-----------------------------------------------------------------------------------------------------------------------------------------------------#

            elif 'downloads' in query or 'download' in query:
                codepath= "C:\\Users\\PC-ASUS\\Downloads\\"
                os.startfile(codepath)          

#-------------------------------------------------None Input-----------------------------------------------------------------------------------------------------------------------------------------------------------#

            # elif '' in query:        
            #     out = 'You Said Nothing'
            #     print(out)
            #     # speak(out) 

#-------------------------------------------------Jokes----------------------------------------------------------------------------------------------------------------------------------------------------------------#

            elif "jokes" in query or "joke" in query:
                joke = pyjokes.get_joke()
                print(joke)
                speak(joke)

#-------------------------------------------------SMS Send-------------------------------------------------------------------------------------------------------------------------------------------------------------#

            elif "send message" in query:
                print("Sir what should i say")
                speak("Sir what should i say")
                msz = takeCommand()

                account_sid = 'AC78333069668be003c756fd46877831e5'
                auth_token = '6d9f8af2ace61d83c37789bc80d4c6eb'
                client = Client(account_sid, auth_token)
                message = client.messages \
                    .create(
                        body=msz,
                        from_='+18457044996',
                        to='+916264032336'
                    )

                print(message.sid)
                print('message sent')
                speak('message sent')

#-------------------------------------------------Call-----------------------------------------------------------------------------------------------------------------------------------------------------------------#

            elif "make a call" in query:

                account_sid = 'AC78333069668be003c756fd46877831e5'
                auth_token = '6d9f8af2ace61d83c37789bc80d4c6eb'
                client = Client(account_sid, auth_token)
                message = client.calls \
                    .create(
                        twiml='<Response><Say>Call Back</Say></Response>',
                        from_='+18457044996',
                        to='+916264032336'
                    )

#-------------------------------------------------Battery Percentage---------------------------------------------------------------------------------------------------------------------------------------------------#

            elif "battery" in query or "power remaining" in query:
                battery = psutil.sensors_battery()
                percentage = battery.percent
                print(f"Sir the system have {percentage} percent battery")
                speak(f"Sir the system have {percentage} percent battery")

#-------------------------------------------------Internet Speed-------------------------------------------------------------------------------------------------------------------------------------------------------#

            elif "internet speed" in query:
                st = speedtest.Speedtest()
                dl = st.download()
                up = st.upload()

                print(f"Sir we have {dl} bits per second downloading speed and {up} bits per second uploading speed")
                speak(f"Sir we have {dl} bits per second downloading speed and {up} bits per second uploading speed")

#-------------------------------------------------Screenshot-----------------------------------------------------------------------------------------------------------------------------------------------------------#

            elif 'screenshot' in query:
                print("Please Tell me the name of the screenshot")
                speak("Please Tell me the name of the screenshot")
                name=takeCommand()
                print("Please hold the screen for few seconds, i am taking screenshot")
                speak("Please hold the screen for few seconds, i am taking screenshot")

                image = pyscreenshot.grab()
                image.show()
                image.save(r'C:\\Users\\PC-ASUS\\Pictures\\rio screenshot\\'+ name +'.png')

#-------------------------------------------------Volume Up------------------------------------------------------------------------------------------------------------------------------------------------------------#

            elif 'volume up' in query:
                io=0
                while(io<10):
                    pyautogui.press("volumeup")
                    io += 1
                print("Volume increased")
                speak("Volume increased")
                io=0

#-------------------------------------------------Volume Down----------------------------------------------------------------------------------------------------------------------------------------------------------#

            elif 'volume down' in query:
                io=0
                while(io<10):
                    pyautogui.press("volumedown")
                    io += 1
                print("Volume decreased")
                speak("Volume decreased")
                io=0

#-------------------------------------------------Volume Mute----------------------------------------------------------------------------------------------------------------------------------------------------------#

            elif 'mute' in query:
                pyautogui.press("volumemute")
                print("Done")
                speak("Done")

#-------------------------------------------------News-----------------------------------------------------------------------------------------------------------------------------------------------------------------#

            elif "news" in query:
                print("Please wait sir, fetching the latest news")
                speak("Please wait sir, fetching the latest news")
                news()

#-------------------------------------------------increase brightness--------------------------------------------------------------------------------------------------------------------------------------------------#

            elif "increase" in query and 'brightness' in query:
                sbc.set_brightness(100)

#-------------------------------------------------decrease brightness--------------------------------------------------------------------------------------------------------------------------------------------------#

            elif "decrease" in query and 'brightness' in query:
                sbc.set_brightness(20)

#-------------------------------------------------switch window--------------------------------------------------------------------------------------------------------------------------------------------------------#

            elif "switch" in query and "window" in query:
                pyautogui.keyDown("alt")
                pyautogui.press("tab")
                time.sleep(1)
                pyautogui.keyUp("alt")

#-------------------------------------------------Close Rio------------------------------------------------------------------------------------------------------------------------------------------------------------#

            elif "exit" in query:
                print("Ok I am going, Have a good Day sir")
                speak("Ok I am going, Have a good Day sir")
                sys.exit()

#-------------------------------------------------shutdown-------------------------------------------------------------------------------------------------------------------------------------------------------------#

            elif 'shutdown' in query:
                out='Shutting Down The System'                                                                                   #|
                print(out)                                                                             #|
                speak(out)
                os.system('shutdown -s')

#-------------------------------------------------restart--------------------------------------------------------------------------------------------------------------------------------------------------------------#

            elif "restart" in query:
                print("Restarting the system")
                speak("Restarting the system")                
                os.system("shutdown /r /t 5")

#-------------------------------------------------sleep mode-----------------------------------------------------------------------------------------------------------------------------------------------------------#
            
            elif "sleep mode" in query:
                print("System is going in sleep mode")
                speak("System is going in sleep mode")  
                os.system("rundll32.exe powrprof.dll,SetSuspendState 0,1,0")

#-------------------------------------------------sign out-------------------------------------------------------------------------------------------------------------------------------------------------------------#

            elif "sign out" in query:
                speak("Ok , your pc will log off in 10 sec make sure you exit from all applications")
                subprocess.call(["shutdown", "/l"])
                    
        time.sleep(3)

#-------------------------------------------------Driver Code----------------------------------------------------------------------------------------------------------------------------------------------------------#

if __name__ == "__main__" :
    widget= Widget()

time.sleep(1)
while 1:
    query= takeCommand()
    speak(query)
engine.runAndWait()


#-------------------------------------------------Code Finish----------------------------------------------------------------------------------------------------------------------------------------------------------#

import datetime
import time
import os,sys
import speech_recognition as sr
import wikipedia
import pyautogui
from google_speech import Speech
from time import ctime
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import Select

def speak(audio):
    print(audio)
    time.sleep(0.3)
    Speech(audio,"en").play(("speed", "1.0"))

def greetMe():
    speak("hello sir,")
    hour=int(datetime.datetime.now().hour)
    if hour>=0 and hour<12:
        speak("Good Morning")
    elif hour>=12 and hour<18:
        speak("Good Afternoon")
    else:
        speak("good evening")
    speak("please tell me how may i help you")

def getCommand():
    r=sr.Recognizer()
    text=""
    with sr.Microphone() as source:
        #speak("listening..")
        print("listening.....")
        r.adjust_for_ambient_noise(source)
        audio=r.listen(source)
        try:
            text = r.recognize_google(audio)
            print("You said : {}".format(text))
            #speak("You said : {}".format(text))
        except:
            print("Sorry could not recognize your voice")
            #speak("Sorry could not recognize your voice")
    return text

def whatsapp():
    driver= webdriver.Firefox(executable_path="/home/dashrath/Desktop/Final_year/geckodriver")
    driver.get('https://web.whatsapp.com/')
    speak(" please scan your qr code....")
    entry=False
    while not entry:
        try:
            entry=driver.find_element_by_xpath('/html/body/div[1]/div/div/div[4]/div/div/div[1]').is_displayed()
        except:
            speak(" please scan your qr code....")
            time.sleep(10)
    speak("hey you want send message for ")
    eloop=True
    query=getCommand()
    while query == "":
        query=getCommand()
    try:
        driver.find_element_by_xpath("//span[contains(@class,'_19RFN')] [contains(@title,'"+query+"')]").click()
    except:
        speak(query+" is not in your contact...")
    speak("what message you want to send...")
    query=getCommand()
    while query =="":
        query=getCommand()
    driver.find_element_by_xpath("/html/body/div[1]/div/div/div[4]/div/footer/div[1]/div[2]/div/div[2]").send_keys(query)
    driver.find_element_by_xpath("/html/body/div[1]/div/div/div[4]/div/footer/div[1]/div[3]/button").click()
    # while eloop:
    #     query=getCommand()
    #     driver.find_element_by_xpath("//span[contains(@class,'_19RFN')] [contains(@title,'"+query+"')]").click()
    #     if "close" in query:
    #         eloop=False    

def ppT():
    # os.popen("libreoffice")
    # speak("which file you want to open ...")
    # query=getCommand()
    # while query=="":
    #     query=getCommand()
    # speak("you want to open "+query+" file right..")
    # query=getCommand()
    # while query=="":
    #     query=getCommand()
    # if 'no' in query:
    #     speak("okay so,")
    os.popen("libreoffice /home/dashrath/Downloads/gradle.odp")
    time.sleep(7)
    loop=True
    while loop:
        query=getCommand()
        if 'slideshow' in query:
            pyautogui.keyDown('fn')
            pyautogui.press('f5')
            pyautogui.keyUp('fn')
        elif query in ["next","second"]:
            pyautogui.press('right')
        elif 'previous' in query:
            pyautogui.press('left')
        elif 'exit' in query:
            pyautogui.press('esc')
        elif 'close' in query:
            pyautogui.keyDown('alt')
            pyautogui.press('f4')
            pyautogui.keyUp('alt')
            loop=False
        else:
            speak("Sorry..")
            # pyautogui.keyDown('alt')
            # pyautogui.press('f4')
            # pyautogui.keyUp('alt')

def createFile():
    os.popen('gedit')
    time.sleep(3)
    loop=True
    pyautogui.click(x=200, y=200)
    while loop:
        query=getCommand()
        pyautogui.write(query+" ")

def performTask(text):
    if "how are you" in text:
        speak("I am fine!..")
        speak("what about you")
    elif "what time it is" in text:
            speak(ctime())
    elif "where is" in text:
        location=""
        text=text.split(" ")
        location=str(location.join(text[2:]))
        speak("Hold on sir I will show you where " +location+ " is.")
        os.system("firefox browser https://www.google.nl/maps/place/" + location + "/&amp;")
    elif "search" in text:
        search=""
        text=text.split(" ")
        search=search.join(text[1:])
        os.system("firefox browser 'https://www.google.co.in/search?q='"+search)    
    elif "screenshot" in text:
        im=pyautogui.screenshot("a.png")
        im.save()
    elif "youtube" in text:
        search=""
        text=text.split(" ")
        search=search.join(text[0:len(text)-1])
        os.system("google-chrome 'https://www.youtube.com/results?search_text='"+search)
    elif 'wikipedia' or 'who is' in text:
        speak('searching wikipedia...')
        print(text)
        text=text.replace('wikipedia','')
        print(text)
        results=wikipedia.summary(text,sentences=2)
        speak('according to wikipedia ..')
        speak(results)
    elif 'play music' in text:
        os.system("mpg321 h.mp3")
    elif "code" in text:
        print("visual")
        os.popen("code")
    elif "whatsapp" in text:
        whatsapp()
    elif ("ppt","presentation") in text:
        ppT()
    else:
        os.system("google-chrome 'https://www.google.co.in/search?q='"+text)

if __name__ == "__main__":
    #greetMe()
    #whatsapp()
    #ppT()
    createFile()
    flag=False
    while flag:
        print("listening......")
        text=getCommand().lower()
        if ["quit","exit","bye"] in text:
            speak('Good Bye Sir, have a good day.')
            flag=False
            sys.exit()
        else:
            performTask(text)



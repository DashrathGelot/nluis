import speech_recognition as sr
from gtts import gTTS       
# import subprocess

# Record Speach
r1 = sr.Recognizer()

with sr.Microphone() as source:
    print('speak now')
    audio = r1.listen(source)
    s = ""
    for i in r1.recognize_google(audio):
        s += i 
    print(s)
    var = gTTS(s,lang='en')
    print("File Saving ...")
    var.save('a.mp3')
    print("Successfully Save.")
    # print("Audio Playing ...")
    # subprocess.call(['afplay','a.mp3'])
    # print("Completed !")
    
    
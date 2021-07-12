import sys,time
import os
import speech_recognition as sr
def animatedtext(text):
    message = text
    def animation(message):
        for char in message:
            sys.stdout.write(char)
            sys.stdout.flush()
            time.sleep(0.1)
    animation(message)

def animatedtextfile(file):
    message = open(file, "r")
    def animation(message):
        for char in message:
            sys.stdout.write(char)
            sys.stdout.flush()
            time.sleep(0.1)
    animation(message)
def voicerec(limit):
    voice= sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        audio = voice.listen(source , phrase_time_limit= limit)
        voicerec.text = voice.recognize_google(audio)
        voicerec.text = voicerec.text.lower()
        print(f"--> {voicerec.text}")
#Platform Check

if os.path.isfile("/bin/pacman") or os.path.isfile("/bin/apt"):
    p = "linux"
if os.path.isfile("/system/build.prop"):
    p = "android"
if os.path.isdir("/windows"):
    p = "windows"
if os.path.isfile("/bin/yay"):
    s = "arch"
if os.path.isfile("/bin/apt"):
    s = "debian"
platform = p
splatform = s #specific Platform
#Get User Name
import getpass
user = getpass.getuser()
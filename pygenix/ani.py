import sys,time
import os
def animatedtext(text,time_sleep):
    message = text
    def animation(message):
        for char in message:
            sys.stdout.write(char)
            sys.stdout.flush()
            time.sleep(time_sleep)
    animation(message + "\n")

def animatedtextfile(file , time_sleep):
    message = open(file, "r")
    def animation(message):
        for char in message:
            sys.stdout.write(char)
            sys.stdout.flush()
            time.sleep(time_sleep)
    animation(message) 

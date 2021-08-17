import sys,time
import os
from tkinter import Button
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
def tk_hover_btn(root,x,y,text,bcolor,fcolor , cmd):
    #taken from --> https://www.youtube.com/watch?v=u8Em9OQJXaI
    def on_enter(e):
        mybutton['background'] = bcolor
        mybutton['foreground'] = fcolor

    def on_leave(e):
        mybutton['background'] = fcolor
        mybutton['foreground'] = bcolor

    mybutton = Button(root,width=22 , height = 2 , text = text , fg = bcolor , bg = fcolor , border = 0 , activeforeground=fcolor , activebackground = bcolor , command = cmd)
    mybutton.bind("<Enter>" , on_enter)
    mybutton.bind("<Leave>" , on_leave)
    mybutton.place(x=x , y=y)
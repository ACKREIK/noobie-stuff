import tkinter as tk
from tkinter import ttk
from tkinter import * 
import os
try: #play sound
    from playsound import playsound
    
except ImportError as e:
    import subprocess
    import sys
    subprocess.check_call([sys.executable, "-m", "pip", "install", "playsound"])
    from playsound import playsound

full_path = os.path.realpath(__file__)


# this is the function called when the button is clicked
def mario():
	playsound(os.path.dirname(full_path)+"\mario.wav")
print(os.path.dirname(full_path)+"\mario.wav")


# this is the function called when the button is clicked
def loogi():
    
	playsound(os.path.dirname(full_path)+"\loogi.wav")


# this is the function called when the button is clicked
def pro():
	playsound(os.path.dirname(full_path)+"\dab.wav")



root = Tk()

# This is the section of code which creates the main window
root.geometry('627x358')
root.configure(background='#F0F8FF')
root.title('dabby lez go!!')


# This is the section of code which creates a button
Button(root, text='mariow!!!', bg='#F0F8FF', font=('arial', 12, 'normal'), command=mario).place(x=46, y=71)


# This is the section of code which creates a button
Button(root, text='loogi!!', bg='#F0F8FF', font=('arial', 12, 'normal'), command=loogi).place(x=290, y=205)


# This is the section of code which creates a button
Button(root, text='dababy', bg='#F0F8FF', font=('arial', 12, 'normal'), command=pro).place(x=376, y=87)


root.mainloop()

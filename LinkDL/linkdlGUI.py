#has support for images, videos and others (text files, etc)
#recco video type is YOUTUBE (ex. https://www.youtube.com/watch?v=PKtnafFtfEo), yes i used a mr beast video haha

#Youtube Continued:
#if you do .mp3 as the file extension for youtube it will become an audio file.
#youtube vids are only mp4s at max quality (max is 720p or the videos max if lower)
#you dont need to add file extensions to youtube mp4s, but for mp3s you do.

# for vids OTHER than youtube there is NO garuntee to work, AT ALL.

info = """
####INFORMATION####

#This has support for images, videos and others (text files, etc)
#Recco video type is YOUTUBE (ex. https://www.youtube.com/watch?v=PKtnafFtfEo), yes i used a mr beast video haha

#Youtube Continued:
#if you do .mp3 as the file extension for youtube it will become an audio file.
#youtube vids are only mp4s at max quality (max is 720p or the videos max if lower)
#you dont need to add file extensions to youtube mp4s, but for mp3s you do.

#For vids OTHER than youtube there is NO garuntee to work, AT ALL.
####END OF INFO####
"""


import tkinter as tk
from tkinter import ttk
from tkinter import * 
from os import link
import getpass
name = getpass.getuser()
import requests
import shutil,os
print("Prepping...")
print("Logged in as... " + name)
print("Welcome!")
print(info)

try: #pytube
    from pytube import YouTube
    
except ImportError as e:
    import subprocess
    import sys
    subprocess.check_call([sys.executable, "-m", "pip", "install", "pytube"])
    subprocess.check_call([sys.executable, "-m", "pip", "install", "--upgrade", "pytube"])
    from pytube import YouTube

    






import ctypes
ctypes.windll.kernel32.SetConsoleTitleW("bro u gay?")





#ending = input("File ending (ex. .png): ")




headers = {
    'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/78.0.3904.108 Safari/537.36'
}
currentDir = os.getcwd()
path = os.path.join(currentDir,'DL')



def dl(url, nametouse):
    attempts = 0
    full_path = os.path.realpath(__file__)
    while attempts < 5:
        try:
            filename = url.split('/')[-1]
            r = requests.get(url,headers=headers,stream=True,timeout=5)
            if r.status_code == 200:
                print("Attempting to write") 
                with open(os.path.join(os.path.dirname(full_path)+"\DL",nametouse),'wb') as f:
                    r.raw.decode_content = True
                    shutil.copyfileobj(r.raw,f)
                    print("Writing")
            print("Saving as " + nametouse + " at " + os.path.dirname(full_path)+"\DL")
           
            return "Finished"
        except Exception as e:
            attempts+=1
            print("sry an error")

shoulduse = None

# this is a function to get the user input from the text input box
def getInputBoxValue():
	userInput = imgfile.get()
	return userInput


# this is a function to get the user input from the text input box
def getInputBoxValuelink():
	userInput = linker.get()
	return userInput

def getbytesleft(currentstream, datachunk, btyes):

    print(str(btyes) + " Bytes left of video")

# this is the function called when the button is clicked
ytcheck = "https://www.youtube.com/"
mp3check = ".mp3"
def Begin():

    
    linktouse = getInputBoxValuelink()
    nametouse = getInputBoxValue() 
    if not ytcheck in linktouse:
        dl(linktouse, nametouse)
    else:
       
        
        print("YT vid found, converting...")
        yt = YouTube(
        linktouse,
        on_progress_callback=getbytesleft,
        allow_oauth_cache=True
    )
    mp3 = None
    if not mp3check in nametouse:
        stream = yt.streams.get_highest_resolution()
        shoulduse = ".mp4"
    if mp3check in nametouse:
        

        nametouse.replace('.mp3', '')

        yt.streams.filter(only_audio=True)
        stream = yt.streams.get_highest_resolution()
        shoulduse = ".mp3"
        mp3 = True
        print("Requested MP3")
    full_path = os.path.realpath(__file__)
    if not mp3 == True:
        loc = stream.download(os.path.dirname(full_path)+"\DL", shoulduse, nametouse)
    else:
        loc = stream.download(os.path.dirname(full_path)+"\DL", shoulduse, nametouse.replace('.mp3', ''))
    print("YT saved at " + loc)
       





root = Tk()

# This is the section of code which creates the main window
root.geometry('834x541')
root.configure(background='#F0F8FF')
root.title('Link Download Application')


# This is the section of code which creates the a label
Label(root, text='Link', bg='#F0F8FF', font=('arial', 12, 'normal')).place(x=49, y=49)


# This is the section of code which creates a text input box
imgfile=Entry(root)
imgfile.place(x=47, y=175)


# This is the section of code which creates the a label
Label(root, text='Image Name (INCLUDES FILE ENDING)', bg='#F0F8FF', font=('arial', 12, 'normal')).place(x=43, y=150)


# This is the section of code which creates a text input box
linker=Entry(root)
linker.place(x=49, y=69)


# This is the section of code which creates a button
Button(root, text='Start', bg='#F0F8FF', font=('arial', 12, 'normal'), command=Begin).place(x=52, y=273)


root.mainloop()

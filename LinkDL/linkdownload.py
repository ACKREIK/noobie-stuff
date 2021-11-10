from os import link
import getpass
name = getpass.getuser()
import requests
import shutil,os

try:
    from getch import pause
except ImportError as e:
    import subprocess
    import sys


    subprocess.check_call([sys.executable, "-m", "pip", "install", "py-getch"])

print("Prepping...")
print("Logged in as... " + name)
print("Welcome!")


linktouse = input("Link: ")
nametouse = input("Name of file (WITH ENDING): ")
#ending = input("File ending (ex. .png): ")



name = getpass.getuser()

headers = {
    'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/78.0.3904.108 Safari/537.36'
}
currentDir = os.getcwd()
path = os.path.join(currentDir,'DL')

def dl(url):
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


if dl(linktouse) == "Finished":
 url = "http://chihuahuaspin.com/"

 #os.startfile(url)
 from getch import pause
 print('Writing to file..')
 pause('Press any key to finish.')
quit()









from random import randint
import requests
from tkinter import messagebox
from bs4 import BeautifulSoup
import os

showcode = False

def codegen():
    global code
    global name2
    global tags2
    code = str(randint(1,440000))
    URL = "https://nhentai-net.translate.goog/g/"+code+"/?_x_tr_sl=auto&_x_tr_tl=en&_x_tr_hl=en-US&_x_tr_pto=wapp" #bratty cloudflare protection needs bypass correction
    page = requests.get(URL)
    soup = BeautifulSoup(page.content, "html.parser")
    name = soup.find("meta", {"name":"twitter:title"})
    tags = soup.find("meta", {"name":"twitter:description"})
    name2 = name["content"]
    tags2 = tags["content"]



    print(code)
    inspect()

def inspect():
    global alert
    blacklistDirectory = os.path.dirname(os.path.abspath(__file__))
    blacklistFile = open(blacklistDirectory+"\\blacklist.txt", "r")
    blacklistread = blacklistFile.read()
    blacklist = blacklistread.split("\n")
    taglist = tags2.split()

    if any(x in blacklist for x in taglist):
        print("Blacklisted tag detected, skipping code "+code+"...")
        codegen()
    else:
        textbox()

    

def textbox():
    global showcode
    text = "Code generated\n"+code+"\n\nName\n"+name2+"\n\nTags\n"+tags2+"\n\nOpen code in Incognito tab or generate another code?"
    showcode = messagebox.askyesno(title="here's your code you degenerate", message=text)

codegen()

while showcode == False:
    codegen()
else: 
    if showcode == True:
        os.system('"C:\\Program Files\Google\Chrome\Application\chrome.exe" --incognito https://nhentai.net/g/'+code)




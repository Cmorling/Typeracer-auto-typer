import re
import sys
import time
from pynput.keyboard import Key, Controller
import requests

keyboard=Controller()

def getWPM(wpm):
    wps = wpm / 60
    cps = float(wps) * 5.9
    return float(1.0 / cps)

def getRt(url):
    rt = url.split('=')[1]
    return rt

def getToken(rt):
    r = requests.get('https://play.typeracer.com/?rt={}'.format(rt))
    selected = re.findall(r'\{.+| | \}', r.text)
    rightString = ""
    for i in selected:
        if 'jsessionid' in i:
            rightString = i
    rightId = re.findall(r'jsessionid=[0-9A-Z]+', rightString)[0].split('=')[1]
    return rightId

def getTypeText(jsessionid, rt):

    r = requests.post('https://play.typeracer.com/gameserv;jsessionid={}?rt={}'.format(jsessionid, rt), data='7|1|8|https://play.typeracer.com/com.typeracer.redesign.Redesign/|F3826187330E89EF6B6D98C5D0993876|_|joinRoom|y|2r|1w|{}|1|2|3|4|2|5|6|5|0|1|0|7|r9sY_zcX|8|'.format(rt), headers={
        'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64; rv:78.0)  Firefox/78.0',
        'Content-Type': 'text/x-gwt-rpc', 
        'Referer': 'https://play.typeracer.com/?rt={}'.format(rt), 
        'X-GWT-Permutation': '608319EE4F5291302E6D97608BA8F311',
        'X-GWT-Module-Base': 'https://play.typeracer.com/com.typeracer.redesign.Redesign/', 
        'Connection': 'close',
        'Accept-Encoding': 'en-US',
        })
    return r.text
    
def sortText(text):	
    wordSorted = re.split('\",\"', text)
    del wordSorted[0]
    phrase = max(wordSorted, key=len)
    typertext = (max(wordSorted, key=len)).encode('utf-8').decode("unicode-escape").encode('ascii').decode('utf-8') 
    wpm = int(input('How fast would you like to go? [<wpm>]'))
    if wpm == "":
        print('[!] SUPPLY VALID WPM ')
        exit()
    pause = getWPM(wpm)
    start= input("Click yes when there are 3 seconds left[y/n]: ")
    if not start == 'y':
        exit()
    print('[*] Starting type')
    time.sleep(3) 
    for i in typertext:
	    keyboard.press(i)
	    keyboard.release(i)
	    time.sleep(pause)

def __main__():    
    url = sys.argv[1]
    print('[?] Parsing RaceTrack')
    rt = getRt(url)

    print('[*] Racetrack found\n')
    print('[?] Initilating client')
    token = getToken(rt)
    print('[*] Token found\n')
    print('[?] Requesting text')
    text = getTypeText(token, rt)
    print('[*] Text retreived\n')
    sortText(text)
    print('[*] Exiting')
__main__()

import re
import sys
import time
from pynput.keyboard import Key, Controller
import requests

keyboard=Controller()
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
    proxies = {
            'http': 'http://127.0.0.1:8080',
            'https': 'http://127.0.0.1:8080'
            }
    r = requests.post('https://play.typeracer.com/gameserv;jsessionid={}?rt={}'.format(jsessionid, rt), data='7|1|8|https://play.typeracer.com/com.typeracer.guest.Guest/|5CBFBDCD9A4D280D027FF3A5E637DC0C|_|joinRoom|y|2r|1w|{}|1|2|3|4|2|5|6|5|0|1|0|7|XRaIrZ0Q|8|'.format(rt), headers={
        'Content-type': 'text/x-gwt-rpc', 
        'Referer': 'https://play.typeracer.com/?rt={}'.format(rt), 
        'X-GWT-Permutation': 'BDBA47CD90E46D67D7DF854CAA005C64',
        'X-GWT-Module-Base': 'https://play.typeracer.com/com.typeracer.guest.Guest/', 
        'Connection': 'close',
        'Accept-Encoding': 'en-US',
        })
    return r.text
    
def sortText(text):	
    wordSorted = re.split('\",\"', text)
    del wordSorted[0]
    phrase = max(wordSorted, key=len)
    typertext = (max(wordSorted, key=len)).encode('utf-8').decode("unicode-escape").encode('ascii').decode('utf-8') 
    start= input("Click yes when there are 3 seconds left[y/n]: ")
    if not start == 'y':
        exit()
    print('[*] Starting type')
    time.sleep(3) 
    for i in typertext:
	    keyboard.press(i)
	    keyboard.release(i)
	    time.sleep(.015)

def __main__():    
    url = sys.argv[1]
    print('[+] Parsing RaceTrack')
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

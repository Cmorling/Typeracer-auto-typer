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
    print(rightId)
    return rightId
            
def typeText(input):
	with open(input, 'r') as file:
		data=file.read().replace('\n', '')	
		wordSorted = re.split('\",\"', data)
		del wordSorted[0]
		phrase = max(wordSorted, key=len)
		print(type(phrase.encode('utf-8')))
		typertext = (max(wordSorted, key=len)).encode('utf-8').decode("unicode-escape").encode('ascii').decode('utf-8')
		time.sleep(2)
		print('')
		for i in typertext:
			keyboard.press(i)
			keyboard.release(i)
			print('printing ' + str(i))
			time.sleep(.012)
def __main__():    
    url = sys.argv[1]
    rt = getRt(url)
    print(rt)
    getToken(rt)
    
__main__()

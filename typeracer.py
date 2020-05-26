import re
import sys
import time
from pynput.keyboard import Key, Controller
import requests
keyboard=Controller()

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
typeText(sys.argv[1])
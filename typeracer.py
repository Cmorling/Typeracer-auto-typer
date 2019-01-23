import re
import sys
import pyperclip
import time
from pynput.keyboard import Key, Controller

keyboard=Controller()

with open(sys.argv[1], 'r') as file:
	data=file.read().replace('\n', '')	
	wordSorted = re.split('\",\"', data)
	del wordSorted[0]
	typertext = (max(wordSorted, key=len)).decode("unicode-escape").encode('ascii')
	time.sleep(2)
	print('')
	for i in typertext:
		keyboard.press(i)
		keyboard.release(i)
		print('printing ' + str(i))
		time.sleep(.02)

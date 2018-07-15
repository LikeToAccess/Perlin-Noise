from noise import pnoise2, pnoise1
from os import system
from time import sleep
import random

width = 26
height = 36

o = 0.5
f = 16.0 * o

octaves = 0.5
freq = 16.0 * octaves + 2
for i in range(10000):
	#octaves =  pnoise1(i/f, 1) + 0.5
	freq -= 0.00123456789
	if freq < 0:
		break
	if freq == 0.0:
		freq += 0.1
	freq = " ".join(str(freq)).split()
	if len(freq) < 13:
		for char in range(13-len(freq)):
			freq.append("0")
	freq = "".join(freq)
	print "zoom: ", freq+"x"
	freq = float(freq)
	for y in range(height):
		for x in range(width):
			n = pnoise2(x/freq,y/freq,1) * 10
			if n >= 1:
				if n >= 1:
					n = "#"
				else:
					n = "#"
			else:
				n = "-"
			print n,
		print
	#sleep(0.01)
	system("clear")
	
	
	
	
	
	

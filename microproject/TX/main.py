import base64 
import numpy as np
import time
from b2bin import b2bin
import serial
from sync import filestart
from sync import filend
duration=0.1
arduino = serial.Serial('/dev/ttyACM0', 9600)
image = open('t.txt', 'rb') #open binary file in read mode
image_read = image.read()
image_64_encode = base64.b64encode(image_read)
a=np.array(list(image_64_encode))

print "synchronising",
for i in range(0,6):
		print ".",
		time.sleep(0.1)

filestart(arduino)

print "transfer process started!"
for i in range(len(a)):
	print "\n"
	print(a[i])
	bin=b2bin(a[i])
	
	for x in range (0,6):
		print bin[x],
		if bin[x]=='1' :
			arduino.write('H') 
		elif bin[x]=='0':
			arduino.write('L')
		time.sleep(duration)

print "\nsending the end of file signal!"
filend(arduino)
arduino.write('Z')
print "process completed!"

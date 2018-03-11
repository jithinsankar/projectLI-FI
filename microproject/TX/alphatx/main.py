import base64 
import numpy as np
import time
from b2bin import b2bin
import serial
duration=1
arduino = serial.Serial('/dev/ttyACM1', 9600)
image = open('t.txt', 'rb') #open binary file in read mode
image_read = image.read()
image_64_encode = base64.b64encode(image_read)
a=np.array(list(image_64_encode))
print "transfer process started!"
for i in range(len(a)):
	print "\n"
	print(a[i])
	bin=b2bin(a[i])
	arduino.write('H')	#start signal
	time.sleep(duration)
	for x in range (0,6):
		arduino.write('H') 
		print bin[x],
		if bin[x]=='1' :
			arduino.write('H') 
		elif bin[x]=='0':
			arduino.write('L')
		time.sleep(duration)
arduino.write('L')
print "process completed!"

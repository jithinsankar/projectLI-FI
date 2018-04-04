import base64 
import numpy as np
import time
from b2bin import b2bin
import serial
import re
duration=1
arduino = serial.Serial('/dev/ttyACM0', 19200)
image = open('t.txt', 'rb') #open binary file in read mode
image_read = image.read()
image_64_encode = base64.b64encode(image_read)
image_64_encode=re.sub('[=]','',image_64_encode)
a=np.array(list(image_64_encode))
print "transfer process started!"

arduino.write('H')
time.sleep(1)
arduino.write('L')
time.sleep(1)

for i in range(len(a)):
	print "\n"
	print(a[i])
	bin=b2bin(a[i])
	arduino.write('H')	#start signal
	if i==0:
		time.sleep(1)
	else:
		time.sleep(duration)
	for x in range (0,6): 
		print bin[x],
		if bin[x]=='1' :
			arduino.write('H') 
		elif bin[x]=='0':
			arduino.write('L')
		time.sleep(duration)
arduino.write('L')
print "process completed!"
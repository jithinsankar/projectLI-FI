import base64 
import numpy as np
import time
from b2bin import b2bin
import serial
from sync import filestart
from sync import filend
arduino = serial.Serial('/dev/ttyUSB1', 9600)
image = open('t.txt', 'rb') #open binary file in read mode
image_read = image.read()
image_64_encode = base64.encodestring(image_read)
					#print image_64_encode
					#np.set_printoptions(threshold=np.nan)
a=np.array(list(image_64_encode))




filestart(arduino)


for i in range(len(a)):
	print(a[i])
	bin=b2bin(a[i])
	
	for x in range (0,6):
		print (bin[x])
		
		if bin[x]==1 :
			arduino.write('H')
		else:
			arduino.write('L')
		time.sleep(0.1)

filend(arduino)
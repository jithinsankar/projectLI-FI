import base64 
import numpy as np
import time
import serial
arduino = serial.Serial('/dev/ttyUSB1', 9600)
image = open('muse.mp3', 'rb') #open binary file in read mode
image_read = image.read()
image_64_encode = base64.encodestring(image_read)
#print image_64_encode
c="B"
np.set_printoptions(threshold=np.nan)
a=np.array(list(image_64_encode))
for i in range(len(a)):
	#print(a[i])
	if (a[i]==c ):
		arduino.write('H')
	else:
		arduino.write('L')	
	time.sleep(0.00001)




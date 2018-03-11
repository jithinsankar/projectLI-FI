import serial
import time
from bin2b import bin2b
arduino = serial.Serial('/dev/ttyACM0', 19200)
duration=0.001
a2=0
High=0
Medium=0
Low=0
a=[]
b=[]
while True:
	a1=arduino.readline()
	a1=int(a1)
	print a1
	time.sleep(duration)
	#print (type(a1))
	if (a1-a2)> 200:
		High=int(a1)
		time.sleep(1)
		Medium=int(arduino.readline())
		time.sleep(1)
		Low=int(arduino.readline())
		time.sleep(1)
		while True:
			if len(a)==8
				b64=bin2b(''.join(a))
				b.append(b64)
				for u in range(0,8)
					del a[u]
			if (arduino.readline() < (High+50)) && (arduino.readline() > (High-50))
				a.append(1)
			elif(arduino.readline() < (Low+50)) && (arduino.readline() > (Low-50))
				a.append(0)
			elif(arduino.readline() < (Medium+50)) && (arduino.readline() > (Medium-50))
				image_64_decode=list(a)
				image_64_decode=''.join(image_64_decode)
				image_64_decode = base64.b64decode(image_64_decode)
				print image_64_decode
				image_result = open('t.txt', 'wb') # create a writable 	image and write the decoding result
				image_result.write(image_64_decode)
				image_result.close()
				break
			time.sleep(duration)	
		a2=a1	
		time.sleep(duration)
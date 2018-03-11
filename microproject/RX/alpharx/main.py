import serial
import time
from bin2b import bin2b
import sys
import base64
arduino = serial.Serial('/dev/ttyACM0', 19200)
duration=1
a2=0
High=0
a=[]
b=[]
while True:
	a1=int(arduino.readline())
	time.sleep(duration)
	print a1

	if a1-a2 > 70:
		High=a1
		print "Docking done ..............................................."
		while  True:
			if len(a)==6 :
				print "a fulfilled"
				b64=bin2b(*a)
				b.append(b64)
				print b64
				b1=int(arduino.readline())
				if (b1 < (High+50)) and (b1 > (High-50)) :
					print "checking for more"
					time.sleep(duration)
				else :
					print "writing"
					print b
					b[0]='e'
					b[1]='g'
					b[2]='o'
					b[3]='='
					time.sleep(2)
					image_64_decode=list(b)
					image_64_decode=''.join(image_64_decode)
					image_64_decode = base64.b64decode(image_64_decode)
					image_result = open('u.txt', 'wb') # create a writable 	image and write the decoding result
					image_result.write(image_64_decode)
					image_result.close()
					print "transfer done"
					time.sleep(3)
					sys.exit()
				for u in range(5,-1,-1):
					del a[u]
					print "deleting a"
			b2=int(arduino.readline())
			if (b2 < (High+50)) and (b2 > (High-50)) :
				a.append(1)
				print "added 1"
			else :
				a.append(0)
				print " added 0"
			time.sleep(duration)
	a2=a1	

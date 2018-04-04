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
rangeby2=30
while True:
	a1=int(arduino.readline())
	if a1-a2 > rangeby2:
	 time.sleep(1)
	else:
		time.sleep(duration)
	print a1

	if a1-a2 > rangeby2:
		High=a1
		print "Docking done ..............................................."
		while  True:
			if len(a)==6 :
				print "a fulfilled"
				b64=bin2b(''.join(a))
				b.append(b64)
				print b64
				b1=int(arduino.readline())
				if (b1 < (High+rangeby2)) and (b1 > (High-rangeby2)) :
					print "checking for more"
					time.sleep(duration)
				else :
					print "writing"
					print b
					time.sleep(2)
					image_64_decode=list(b)
					while len(image_64_decode)%4 !=0 :					###########
						image_64_decode+='='	
					image_64_decode=''.join(image_64_decode)
					image_64_decode = base64.b64decode(image_64_decode)
					print image_64_decode
					image_result.close()
					print "transfer done"
					time.sleep(3)
					sys.exit()
				for u in range(5,-1,-1):
					del a[u]
					print "deleting a"
			b2=int(arduino.readline())
			if (b2 < (High+rangeby2)) and (b2 > (High-rangeby2)) :
				a.append('1')
				print "added 1"
			else :
				a.append('0')
				print " added 0"
			time.sleep(duration)
	a2=a1	

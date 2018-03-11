import serial
import time
arduino = serial.Serial('/dev/ttyACM0', 19200)
duration=1
a1=0
a2=0
while True:
	a1=int(arduino.readline())
	time.sleep(duration)
	print a1
	if a1-a2 > 70:
		High=a1
		print "Docking done ..............................................."
		while True:
			a1=int(arduino.readline())
			time.sleep(duration)
			if (a1 < (High+50)) and (a1 > (High-50)) :
				print "High"
			else :
				print "low"
	a2=a1

'''while True:
	a1=int(arduino.readline())
	if(a1 < (200)) and (a1 > (100)) :
		print "H"
	else :
		print "l"
'''
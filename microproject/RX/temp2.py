import serial
import time
arduino = serial.Serial('/dev/ttyACM0', 19200)
duration=0.01
a2=0
High=0
for x in xrange(1,1000):
	pass
	a1=arduino.readline().strip()
	a1=int(a1)
	print a1
	time.sleep(duration)
		'''	#print (type(a1))
		if (a1-a2)> 200:
		High=int(a1)
			time.sleep(1)
		Medium=int(arduino.readline())
		time.sleep(1)
		Low=int(arduino.readline())
		time.sleep(1)'''
	a2=a1
	time.sleep(duration)
print (High)'''
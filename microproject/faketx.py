import serial
import time
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
	print a1
	a1=int(a1)
	print a1
			
	#print (type(a1))
	if (a1-a2)> 100:
		High=int(a1)
		print High
		#time.sleep(1)
		Medium=int(arduino.readline())
		time.sleep(1)
		Low=int(arduino.readline())
		time.sleep(1)
		break
	time.sleep(duration)
	a2=a1
print High
print Medium
print Low
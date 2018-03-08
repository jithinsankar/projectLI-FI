import serial
import time
def filestart(arduino):
	for x in range (0,1):
		arduino.write('H')
		time.sleep(1)
		arduino.write('M')
		time.sleep(1)
		arduino.write('L')
		time.sleep(1)
	print "sending the start signal"


def filend(arduino):
	arduino.write('M')
	time.sleep(2)
	arduino.write('Z')

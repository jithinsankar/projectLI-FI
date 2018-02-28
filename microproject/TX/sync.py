import serial
import time
def filestart(arduino):
	for x in range (0,3):
		arduino.write('H')
		time.sleep(1)
		arduino.write('M')
		time.sleep(1)
		arduino.write('L')
		time.sleep(1)
	print "sending the start signal"	
	arduino.write('M')
	time.sleep(2)


def filend(arduino):
	arduino.write('M')
	time.sleep(2)
	arduino.write('Z')

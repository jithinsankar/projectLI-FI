import serial
import time
arduino = serial.Serial('/dev/ttyACM0', 19200)
duration=1
a1=0
a2=0
while True:
	print (arduino.readline())
	time.sleep(0)
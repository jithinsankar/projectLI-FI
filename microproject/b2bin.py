import time
def b2bin(x):
    return {
        'A': "000000",
        'B': "000001",
    }.get(x, 9) 

c=raw_input("write")

bin=b2bin(c)


for x in range (0,6):
	print (bin[x])
	time.sleep(0.1)

import base64 
import numpy as np
import time
from b2bin import b2bin
image = open('t.txt', 'rb') #open binary file in read mode
image_read = image.read()
image_64_encode = base64.encodestring(image_read)
					#print image_64_encode
					#np.set_printoptions(threshold=np.nan)
a=np.array(list(image_64_encode))
for i in range(len(a)):
	print(a[i])
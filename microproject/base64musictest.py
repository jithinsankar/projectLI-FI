import base64 
import numpy as np
import time

image = open('muse.mp3', 'rb') #open binary file in read mode
image_read = image.read()
image_64_encode = base64.encodestring(image_read)
					#print image_64_encode
					#np.set_printoptions(threshold=np.nan)
a=np.array(list(image_64_encode))
#for i in range(len(a)):
#    print(a[i])
#    time.sleep(0.000001)

image_64_decode=list(a)
image_64_decode=''.join(image_64_decode)

image_64_decode = base64.decodestring(image_64_decode)
print image_64_decode

image_result = open('muse2.mp3', 'wb') # create a writable image and write the decoding result
image_result.write(image_64_decode)
image_result.close()





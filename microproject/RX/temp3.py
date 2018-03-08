import numpy as np
import base64
a=[]
a.append('a')
a.append('G')
a.append('U')
a.append('K')
image_64_decode=list(a)
image_64_decode=''.join(image_64_decode)
image_64_decode = base64.b64decode(image_64_decode)
print image_64_decode

image_result = open('t.txt', 'wb') # create a writable image and write the decoding result
image_result.write(image_64_decode)
image_result.close()
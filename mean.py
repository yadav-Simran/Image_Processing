import cv2
import matplotlib.pyplot as plt
import numpy as np
img=cv2.imread('D:\python with simran\Image P\Lenna_(test_image).png',0)
l,b=img.shape
output=np.zeros((l,b),np.uint8())
result =0
for j in range (2,l-2):
    for i in range(2,b-2):
        for y in range(-2,3):
            for x in range(-2,3):
                result+=img[j+y,i+x]
        output [j][i]=int(result/25)
        result=0

plt.imshow(output,cmap='gray')
plt.show()
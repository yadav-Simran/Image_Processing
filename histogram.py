# import cv2, numpy, matplotlib
import cv2
import numpy as np
import matplotlib.pyplot as plt
img = cv2.imread('D:\python with simran\Image P\Lenna_(test_image).png', 0)
m, n = img.shape
def hist_plot(img):
        count =[]
        r = []
        for k in range(0, 256):
                r.append(k)
                count1 = 0
                for i in range(m):
                        for j in range(n):
                                if img[i, j]== k:
                                        count1+= 1
                count.append(count1)
        return (r, count)
r1, count1 = hist_plot(img)
# plotting the histogram
plt.stem(r1, count1)
plt.xlabel('intensity value')
plt.ylabel('number of pixels')
plt.title('Histogram of the original image')
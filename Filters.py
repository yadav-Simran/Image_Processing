import numpy as np #numpy library
import matplotlib.pyplot as pyplot #help for visualizatn of data
import random 
import cv2 #stands for open cv
import math 

from cv2 import COLOR_BGR2GRAY, cvtColor, imread, imshow, waitKey
from numpy import dot, exp, mgrid, pi, ravel, square, uint8, zeros


from PIL import Image # pillow library for graphical representatn

def SaltAndPepper(image, density): #this func will create noise in the image 
    output = np.zeros(image.shape, np.uint8) #uint is unsigned int. here this creates a empty 2d array
    threshold = 1 - density 

    for i in range (image.shape[0]):
        for j in range(image.shape[1]):
            possibility=random.random()
            if possibility < density:
                output[i][j]=0
            elif possibility > threshold:
                output[i][j]=255
            else:
                output[i][j]=image[i][j]
    return output

cv2.imshow('image with noise', output)
cv2.waitKey(0)
cv2.destroyAllWindows()

#
    
    #line 14 to 19 is for implementng noise
'''
def MeanFilter(image, filter_size):
    output = np.zeros(image.shape, np.uint8)
    result 0

    #filter size
    if filter_size == 9:
        for j in range (1,image.shape[0]-1):
            for i in range (1,image.shape[0]-1)


'''
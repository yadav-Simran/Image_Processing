# import cv2
# import numpy as np

# # orginal image
# img = cv2.imread('D:\python with simran\Image P\Lenna_(test_image).png',0)
# img = img/255

# cv2.imshow('original image', img)
# cv2.waitKey(0)
# cv2.destroyAllWindows()

# # blank image
# x,y = img.shape
# g = np.zeros((x,y), dtype=np.float32)

# # salt and pepper amount
# pepper = 0.1
# salt = 0.95

# # create salt and peper noise image    
# for i in range(x):
#     for j in range(y):
#         rdn = np.random.random()
#         if rdn < pepper:
#             g[i][j] = 0
#         elif rdn > salt:
#             g[i][j] = 1
#         else:
#             g[i][j] = img[i][j]

# cv2.imshow('image with noise', g)
# cv2.waitKey(0)
# cv2.destroyAllWindows()

import cv2
import numpy as np


## original image
img = cv2.imread('D:\python with simran\Image P\Lenna_(test_image).png', 0)
img = img/img.max() # normalize the pixel value (0~1)

## noise image
# Gaussian Noise
# =============================================================================
# x, y = img.shape
# mean = 0
# var = 0.01
# sigma = np.sqrt(var)
# n = np.random.normal(loc=mean, 
#                      scale=sigma, 
#                      size=(x,y))
# img_noise = img + n
# =============================================================================

# Salt and Pepper Noise
x,y = img.shape
g = np.zeros((x,y), dtype=np.float32)
pepper = 0.1
salt = 0.9  
for i in range(x):
    for j in range(y):
        rdn = np.random.random()
        if rdn < pepper:
            g[i][j] = 0
        elif rdn > salt:
            g[i][j] = 1
        else:
            g[i][j] = img[i][j]

img_noise = g

# preview the images
cv2.imshow('Original Image', img)
cv2.imshow('Image + Noise', img_noise)

cv2.waitKey(0)
cv2.destroyAllWindows()

## denoise image
# mean filter (average)
m = 5
n = 5
denoise_mean = cv2.blur(img_noise, (m,n))

#cv2.imshow('Original Image', img)
cv2.imshow('Image + Noise', img_noise)
cv2.imshow('Denoise Mean', denoise_mean)


cv2.waitKey(0)
cv2.destroyAllWindows()
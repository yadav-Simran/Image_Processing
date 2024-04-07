import numpy as np
from PIL import Image
import matplotlib.pyplot as plt

img = np.array(Image.open('D:\python with simran\Image P\Lenna_(test_image).png')).astype(np.uint8)
grayimg = np.round(0.299 * img[:,:,0] + 0.587 * img[:,:,1]+ 0.114 * img[:,:,2])
h, w = grayimg.shape

horizontal = np.array([[-1, 0, 1], [-2, 0, 2], [-1, 0, 1]])
vertical = np.array([[-1, -2, -1], [0, 0, 0], [1, 2, 1]])


newhorizontalImage = np.zeros((h, w))
newverticalImage = np.zeros((h, w))
newgradientImage = np.zeros((h, w))

for i in range(1, h-1):
    for j in range(1, w-1):
        horizontalGrad = (horizontal[0,0] * grayimg[i-1, j - 1]) + \
            (horizontal[0, 1] * grayimg[i-1, j]) + \
                (horizontal[0, 2] * grayimg[i-1, j+1]) + \
                    (horizontal[1,0] * grayimg[i-1, j - 1]) + \
            (horizontal[1, 1] * grayimg[i-1, j]) + \
                (horizontal[1, 2] * grayimg[i-1, j+1]) + \
                    (horizontal[2, 0] * grayimg[i+1, j - 1]) + \
            (horizontal[2, 1] * grayimg[i+1, j]) + \
                (horizontal[2, 2] * grayimg[i+1, j+1])

        newhorizontalImage[i - 1, j - 1] = abs(horizontalGrad)

        verticalGrad = (vertical[0,0] * grayimg[i-1, j - 1]) + \
            (vertical[0, 1] * grayimg[i-1, j]) + \
                (vertical[0, 2] * grayimg[i-1, j+1]) + \
                    (vertical[1,0] * grayimg[i-1, j - 1]) + \
            (vertical[1, 1] * grayimg[i-1, j]) + \
                (vertical[1, 2] * grayimg[i-1, j+1]) + \
                    (vertical[2, 0] * grayimg[i+1, j - 1]) + \
            (vertical[2, 1] * grayimg[i+1, j]) + \
                (vertical[2, 2] * grayimg[i+1, j+1])
        newverticalImage[i - 1, j - 1] = abs(verticalGrad)

        mag = np.sqrt(pow(horizontalGrad, 2.0) + pow(verticalGrad, 2.0))
        newgradientImage [i - 1, j - 1] = mag

plt.figure()
plt.title("Lenna-after-Sobel.png")
plt.imsave('Lenna-Sobel.png', newgradientImage, cmap = 'gray', format='png')
plt.imshow(newgradientImage, cmap='gray')
plt.show()

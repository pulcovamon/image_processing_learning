import cv2
import numpy as np
import matplotlib.pyplot as plt

img = plt.imread('nature.png')
img = cv2.cvtColor(img, cv2.COLOR_RGB2GRAY)
'''
plt.imshow(img)
plt.show()

cv2.imshow('grayscale', img)
cv2.waitKey(0)
'''
histogram = plt.hist(img.ravel(), bins=256, range=(0.0, 1.0), fc='k', ec='k')
plt.show()

# reads an input image
img = cv2.imread('image.jpg',0)

# find frequency of pixels in range 0-255
histr = cv2.calcHist([img],[0],None,[256],[0,256])
  
# show the plotting graph of an image
plt.plot(histr)
plt.show()
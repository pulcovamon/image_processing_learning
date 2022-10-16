import cv2
import numpy as np

img = cv2.imread('bug.jpg')

# It converts the BGR color space of image to HSV color space
hsv = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)
     
# Threshold of blue in HSV space
lower_red = np.array([0, 1, 1])
upper_red = np.array([20, 255, 255])

# preparing the mask to overlay
mask = cv2.inRange(hsv, lower_red, upper_red)

# The black region in the mask has the value of 0,
# so when multiplied with original image removes all non-blue regions
result = cv2.bitwise_and(img, img, mask = mask)

cv2.imshow('orig', img)
cv2.imshow('mask', mask)
cv2.imshow('result', result)
cv2.waitKey(0)
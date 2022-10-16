import cv2
import numpy as np

img = cv2.imread('image.jpg')

img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

thresh1 = cv2.adaptiveThreshold(img, 255, cv2.ADAPTIVE_THRESH_MEAN_C, cv2.THRESH_BINARY, 199, 5)
thresh2 = cv2.adaptiveThreshold(img, 255, cv2.ADAPTIVE_THRESH_GAUSSIAN_C, cv2.THRESH_BINARY, 199, 5)

ret, thresh3 = cv2.threshold(img, 120, 255, cv2.THRESH_BINARY)

cv2.imshow('Adaptive Mean', thresh1)
cv2.imshow('Adaptive Gaussian', thresh2)
cv2.imshow('normal threshold', thresh3)

cv2.waitKey(0)
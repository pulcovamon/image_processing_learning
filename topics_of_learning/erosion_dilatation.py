import cv2
import numpy as np

img = cv2.imread('planet.png')
img = cv2.resize(img, (0, 0), fx = 0.3, fy = 0.3)

kernel = np.ones((5, 5), np.uint8)

img_erosion = cv2.erode(img, kernel, iterations = 1)
img_dilatation = cv2.dilate(img, kernel, iterations = 1)
img_result1 = cv2.erode(img_dilatation, kernel, iterations = 1)
img_result2 = cv2.dilate(img_erosion, kernel, iterations = 1)

cv2.imshow('orig', img)
cv2.imshow('erosion', img_erosion)
cv2.imshow('dilatation', img_dilatation)
cv2.imshow('dilatation + erosion', img_result1)
cv2.imshow('erosion + dilatation', img_result2)
cv2.waitKey(0)
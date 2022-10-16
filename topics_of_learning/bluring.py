import cv2
import numpy as np

img = cv2.imread('image.jpg')

# gaussian blur
img_gaussian = cv2.GaussianBlur(img, (7, 7), 0)
cv2.imshow('Gaussian bluring', img_gaussian)
cv2.waitKey(0)

# median blur
img_median = cv2.medianBlur(img, 5)
cv2.imshow('median bluring', img_median)
cv2.waitKey(0)

# bilateral bluring
img_bilateral = cv2.bilateralFilter(img, 9, 75, 75)
cv2.imshow('bilateral bluring', img_bilateral)
cv2.waitKey(0)

cv2.destroyAllWindows()
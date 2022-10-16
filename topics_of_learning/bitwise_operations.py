import numpy as np
import cv2

img1 = np.ones((500, 500), dtype = np.uint8) * 255
img1[:, 250:] = 0

img2 = np.ones((500, 500), dtype = np.uint8) * 255
img2[150:350, 150:350] = 0

imgs_and = cv2.bitwise_and(img1, img2, mask = None)

cv2.imshow('and', imgs_and)
cv2.waitKey(0)

imgs_or = cv2.bitwise_or(img1, img2, mask = None)

cv2.imshow('or', imgs_or)
cv2.waitKey(0)

imgs_xor = cv2.bitwise_xor(img1, img2, mask = None)

cv2.imshow('xor', imgs_xor)
cv2.waitKey(0)

img1_not = cv2.bitwise_not(img1, mask = None)

cv2.imshow('not 1', img1_not)
cv2.waitKey(0)

img2_not = cv2.bitwise_not(img2, mask = None)

cv2.imshow('not 2', img2_not)
cv2.waitKey(0)

cv2.destroyAllWindows()
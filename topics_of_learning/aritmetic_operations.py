from numbers import Rational
import cv2
import numpy as np

img1 = cv2.imread('planet.png')
img2 = cv2.imread('monkey.jpg')

size1 = [max(img1.shape[0],img2.shape[0]), max(img1.shape[1], img2.shape[1])]   # find bigger lenght and high of both image
size2 = [min(img1.shape[0],img2.shape[0]), min(img1.shape[1], img2.shape[1])]   # find smaller lenght and high of both image

print(size1, size2)

ratio = size2[0] / size1[0]                                                     # ratio of smaller lenght and bigger lenght
dim = (size2[1], int(size1[0] * ratio))                                         # new size of the images
img1 = cv2.resize(img1, dim)
img2 = cv2.resize(img2, dim)

print(img1.shape, img2.shape)

weight_sum = cv2.addWeighted(img1, 0.5, img2, 0.4, 0)                           # 0.5 and 0.4 are weights of the original imeges
cv2.imshow('image', weight_sum)
cv2.waitKey(0)
cv2.destroyAllWindows()

img_white = np.ones(img2.shape, dtype=np.uint8) * 255                           # make 3d matrix with the same shape as img2 and filled with 255 in uint8 format
substracted_img = cv2.subtract(img_white, img2)
cv2.imshow('image', substracted_img)
cv2.waitKey(0)
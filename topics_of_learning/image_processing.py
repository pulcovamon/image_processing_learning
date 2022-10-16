import cv2
import numpy as np

FILE_NAME = 'image.jpg'

# scaling image
try:
    img = cv2.imread(FILE_NAME)

    (height, width) = img.shape[:2]     # get number of pixels horizontaly and vertically

    # specify the size and interpolation method
    # cv2.INTER_AREA is used for shrinking
    # cv2.INTER_CUBIC is used for zooming
    img_res = cv2.resize(img, (int(width / 2), int(height / 2)), interpolation = cv2.INTER_CUBIC)

    cv2.imwrite('result.jpg', img_res)    # write image back to disk

except IOError:
    print('Error while reading files!')


# rotating image

try:
    img = cv2.imread(FILE_NAME)

    (rows, cols) = img.shape[:2]

    # create a matrix for transformation
    # rotation w.r.t center to 45 degree without scaling
    matrix = cv2.getRotationMatrix2D((cols / 2, rows / 2), 45, 1)
    img_res = cv2.warpAffine(img, matrix, (cols, rows))

    cv2.imwrite('result.jpg', img_res)

except IOError:
    print('Error while reading file!')

# translating image (shifting it within a given frame of reference)

# create translation matrix, shift: (x, y)
# M = [1 0 x]
#     [0 1 y]
# shift by (100, 50)
matrix = np.float32([[1, 0, -100], [0, 1, 50]])

try:
    img = cv2.imread('image.jpg')
    (rows, cols) = img.shape[:2]

    # warpAffine does shifting when given translation matrix
    img_res = cv2.warpAffine(img, matrix, (cols, rows))

    cv2.imwrite('result.jpg', img_res)

except IOError:
    print('Error while reading files!')

# edge detection

try:
    img = cv2.imread('bug.jpg')
    
    # Canny edge detection
    edges = cv2.Canny(img, 100, 200)          # (image, threshold1, threshold2)
    # 1: high threshold value of intensity gradient
    # 2: low threshold value of intensity gradient

    cv2.imshow('edge detection', edges)
    cv2.waitKey(0)

    cv2.imwrite('result.jpg', edges)

except IOError:
    print ('Error while reading files!')

'''
Canny method for edge detection:

1) noise reduction using 5x5 gaussian filter
larger kernel - smaller sensitivity to noise, increase error of edge detection

2) finding intensity gradient
four filters with a Sobel kernel - vertical, horizontal and two diagonal directions

3) non-maximum suppresion - find the largest edge
all gradient values except local maxima set to 0
check if it is local maximum in its neighborhood in the direction of gradient (removes unwanted pixels which may not constitute the edge)

4) hysteresis thresholding - decide which edges are really edges (removes small pixel noises - edges are long lines)
max value: edges with intensity gradient above this level -> edges 
min value: edges bellow this level -> non-edges
between thresholds: if connected to the sure-edge -> edge, if not -> non-edge
'''
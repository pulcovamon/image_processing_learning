
import cv2
import numpy as np
  
# Open the image.
img = cv2.imread('low_contrast.png')

# Apply log transform.
c = 255/np.log(1 + np.max(img))
log_transformed = c * np.log(1 + img)
  
# Specify the data type.
log_transformed = np.array(log_transformed, dtype = np.uint8)
  
cv2.imshow('transformed', log_transformed)
cv2.waitKey(0)
cv2.destroyAllWindows()

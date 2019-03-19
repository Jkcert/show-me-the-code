import cv2
import numpy as np
img = cv2.imread('mmexport1502109886761.jpg')
shape = img.shape
font = cv2.FONT_HERSHEY_SIMPLEX
cv2.putText(img, '6', ((int)(shape[0] * 0.5), (int)(shape[1] * 0.5)), font, 3, (0, 255, 255), 2, cv2.LINE_AA)
winname = 'number'
cv2.namedWindow(winname)
cv2.imshow(winname, img)
cv2.waitKey(0)
cv2.destroyAllWindows()
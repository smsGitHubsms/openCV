import cv2
import numpy as np
image = cv2.imread("lena.jpg",1)
# blur_image = cv2.blur(image,(5,5))
blur_image = cv2.GaussianBlur(image,(5,5),0)
cv2.imshow("image",image)
cv2.imshow("NewImage",blur_image)
cv2.waitKey(0)
cv2.destroyAllWindows()
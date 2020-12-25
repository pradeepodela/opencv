import cv2
import numpy as np

img = cv2.imread("img.jpg")
kernel = np.ones((5,5),np.uint8)

imgGray = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)# to clor rgb to gray
imgBlur = cv2.GaussianBlur(imgGray,(7,7),0)#note to be even numbers
imgCanny = cv2.Canny(img,100,100)#thick ness
imgDialation = cv2.dilate(imgCanny,kernel,iterations=2)
imgEroded = cv2.erode(imgDialation,kernel,iterations=1)

cv2.imshow("Gray Image",imgGray)
cv2.imshow("Blur Image",imgBlur)
cv2.imshow("Canny Image",imgCanny)
cv2.imshow("Dialation Image",imgDialation)
cv2.imshow("Eroded Image",imgEroded)
cv2.waitKey(0)

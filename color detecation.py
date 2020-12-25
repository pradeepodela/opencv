
import cv2
import numpy as np
def empty(a):
    pass
cap= cv2.VideoCapture(0)



def stackImages(scale,imgArray):
    rows = len(imgArray)
    cols = len(imgArray[0])
    rowsAvailable = isinstance(imgArray[0], list)
    width = imgArray[0][0].shape[1]
    height = imgArray[0][0].shape[0]
    if rowsAvailable:
        for x in range ( 0, rows):
            for y in range(0, cols):
                if imgArray[x][y].shape[:2] == imgArray[0][0].shape [:2]:
                    imgArray[x][y] = cv2.resize(imgArray[x][y], (0, 0), None, scale, scale)
                else:
                    imgArray[x][y] = cv2.resize(imgArray[x][y], (imgArray[0][0].shape[1], imgArray[0][0].shape[0]), None, scale, scale)
                if len(imgArray[x][y].shape) == 2: imgArray[x][y]= cv2.cvtColor( imgArray[x][y], cv2.COLOR_GRAY2BGR)
        imageBlank = np.zeros((height, width, 3), np.uint8)
        hor = [imageBlank]*rows
        hor_con = [imageBlank]*rows
        for x in range(0, rows):
            hor[x] = np.hstack(imgArray[x])
        ver = np.vstack(hor)
    else:
        for x in range(0, rows):
            if imgArray[x].shape[:2] == imgArray[0].shape[:2]:
                imgArray[x] = cv2.resize(imgArray[x], (0, 0), None, scale, scale)
            else:
                imgArray[x] = cv2.resize(imgArray[x], (imgArray[0].shape[1], imgArray[0].shape[0]), None,scale, scale)
            if len(imgArray[x].shape) == 2: imgArray[x] = cv2.cvtColor(imgArray[x], cv2.COLOR_GRAY2BGR)
        hor= np.hstack(imgArray)
        ver = hor
    return ver

cv2.namedWindow("trackbars")
cv2.resizeWindow("trackbars",440,440)
cv2.createTrackbar("hue_min","trackbars",86,179,empty)
cv2.createTrackbar("hue_max","trackbars",0,179,empty)
cv2.createTrackbar("stat_min","trackbars",255,255,empty)
cv2.createTrackbar("stat_max","trackbars",0,255,empty)
cv2.createTrackbar("val_min","trackbars",255,255,empty)
cv2.createTrackbar("val_max","trackbars",114,255,empty)
while True:
    success, img = cap.read()
    #img = cv2.imread("lambo.png")
    h_mn= cv2.getTrackbarPos("hue_min","trackbars")
    h_mx= cv2.getTrackbarPos("hue_max","trackbars")
    s_mn= cv2.getTrackbarPos("stat_min","trackbars")
    s_mx= cv2.getTrackbarPos("stat_max","trackbars")
    v_mn= cv2.getTrackbarPos("val_min","trackbars")
    v_mx= cv2.getTrackbarPos("val_max","trackbars")

    print(h_mn,h_mx,s_mn,s_mx,v_mn,v_mx)

    max =np.array([h_mx,s_mx,v_mx])
    min = np.array([h_mn,s_mn,v_mn])
    maskimg = cv2.inRange(img,max,min)

    imgresult = cv2.bitwise_and(img,img,mask=maskimg)
    iimg = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)


    #cv2.imshow("Result", img)
    if cv2.waitKey(1) and 0xFF == ord('q'):
        break

    imghor = stackImages(0.5,([img,iimg],[imgresult,maskimg]))
    cv2.imshow("win",imghor)
    '''
    cv2.imshow("win",iimg)
    cv2.imshow("inital image",img)
    cv2.imshow("inital image",imgresult)
    cv2.imshow("win",maskimg)'''
    cv2.waitKey(1)

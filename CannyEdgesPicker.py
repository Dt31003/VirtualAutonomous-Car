import cv2
import numpy as np
from scipy import ndimage
import matplotlib.pyplot as plt

def empty(a):
    pass

cv2.namedWindow("CannyEdge")
cv2.resizeWindow("CannyEdge", 640, 240)
cv2.createTrackbar("Min Edge Val", "CannyEdge", 0, 255, empty)
cv2.createTrackbar("Max Edge Val", "CannyEdge", 0, 255, empty)
cv2.createTrackbar("Sobel delta", "CannyEdge", 0, 255, empty)

## ? For realtime video
#cap = cv2.VideoCapture(0, cv2.CAP_DSHOW)

## ? For videos
cap = cv2.VideoCapture("Eurotruck_view4.mp4")

## Sobel parameters
depth = cv2.CV_16S
scale = 1

scale_img = 0.5

while True:    
    ret, img = cap.read()
    
    frameWidth = int(img.shape[1]*scale_img)
    frameHeight = int(img.shape[0]*scale_img)
    
    if ret == False:
        cap = cv2.VideoCapture("Eurotruck_view4.mp4")
        ret, img = cap.read()
        
    img = cv2.resize(img, (frameWidth, frameHeight))
    #img = cv2.flip(img, 0)
    
    ## img processing for canny edge detection
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    kernel = 5
    img_bur = cv2.GaussianBlur(gray, (kernel,kernel), 0)
       
    minVal = cv2.getTrackbarPos("Min Edge Val", "CannyEdge")
    maxVal = cv2.getTrackbarPos("Max Edge Val", "CannyEdge")
    delta = cv2.getTrackbarPos("Sobel delta", "CannyEdge")
    
    canny = cv2.Canny(img_bur, minVal, maxVal)
    
    ## img processing for sobel filter
    gradient_x = cv2.Sobel(img_bur, depth, 1, 0, ksize=3, scale=scale, delta=delta, borderType=cv2.BORDER_DEFAULT)
    gradient_y = cv2.Sobel(img_bur, depth, 0, 1, ksize=3, scale=scale, delta=delta, borderType=cv2.BORDER_DEFAULT)
    
    abs_gradient_x = cv2.convertScaleAbs(gradient_x)
    abs_gradient_y = cv2.convertScaleAbs(gradient_y)
    
    gradient = cv2.addWeighted(abs_gradient_x, 0.5, abs_gradient_y, 0.5, 0)
    
    ## Canny post sobel filter
    canny_post_sobel = cv2.Canny(gradient, minVal, maxVal)
    
    print(f'Edge Value = min: {minVal}, max: {maxVal}')    
    
    cv2.imshow('Original', img)
    cv2.imshow('SobelFilter', gradient)
    cv2.imshow('Canny', canny)
    cv2.imshow('Canny_Post_sobel', canny_post_sobel)
    
    
    k = cv2.waitKey(25)
    if k == 27:
        break

cap.release()
cv2.destroyAllWindows()
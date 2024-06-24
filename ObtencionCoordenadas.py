import cv2
import os
import numpy as np

##### VIDEO

# cap = cv2.VideoCapture(0)

# while True:
#     _, img = cap.read()
    
#     def on_EVENT_LBUTTONDOWN(event, x, y, flags, param):
#         if event == cv2.EVENT_LBUTTONDOWN:
#             xy = "%d,%d" % (x, y)
#             cv2.circle(img, (x, y), 1, (255, 0, 0), thickness = -1)
#             cv2.putText(img, xy, (x, y), cv2.FONT_HERSHEY_PLAIN, 1.0, (0,0,0), thickness = 1)
#             cv2.line(img, (0,y), (img.shape[0],y), (0,0,255),thickness = 1)
#             print(f'Point = x: {x}, y: {y}')
#             cv2.imshow("image", img)
        
#     cv2.imshow("image", img)
#     cv2.namedWindow("image")
#     cv2.setMouseCallback("image", on_EVENT_LBUTTONDOWN)
    
#     S = img.shape
    
#     k = cv2.waitKey(1)
#     if k == 27:
#         break
    
#     if k == 32:
#         print(f'Shape: w: {S[1]}, h: {S[0]}, channels: {S[2]}')
    
# cv2.destroyAllWindows()


###### IMAGEN
cap = cv2.VideoCapture("Eurotruck_view4.mp4")
_, img = cap.read()
# img=cv2.imread(os.path.join('.','VSCODING','Images','Pizzaron.jpg'))
scale = 0.5
img = cv2.resize(img, (int(img.shape[1]*scale), int(img.shape[0]*scale)))

def on_EVENT_LBUTTONDOWN(event, x, y, flags, param):
    if event == cv2.EVENT_LBUTTONDOWN:
        xy = "%d,%d" % (x, y)
        cv2.circle(img, (x, y), 1, (255, 0, 0), thickness = -1)
        cv2.putText(img, xy, (x, y), cv2.FONT_HERSHEY_PLAIN, 1.0, (0,0,0), thickness = 1)
        cv2.line(img, (0,y), (img.shape[1],y), (0,0,255),thickness = 1)
        cv2.line(img, (x,0), (x,img.shape[0]), (0,0,255),thickness = 1)
        print(f'Point = x: {x}, y: {y}')
        cv2.imshow("image", img)
        
cv2.namedWindow("image")
cv2.setMouseCallback("image", on_EVENT_LBUTTONDOWN)

S = img.shape

cv2.imshow("image", img)
cv2.waitKey(0)

k = cv2.waitKey(1)
    
if k == 32:
    print(f'Shape: w: {S[1]}, h: {S[0]}, channels: {S[2]}')
    
cv2.destroyAllWindows()
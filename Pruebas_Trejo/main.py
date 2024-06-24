import cv2
import numpy as np
import Birdseye
import transformations as tf
import laneDetection as ld

ref_points = [(299,527),(422,342),
              (540,342), (654,527)]

## ?  reference points = [bl, tl, tr, br]

#Change perspective to birdseye
def change_perspective(image):
    h = image.shape[0]
    w = image.shape[1]
    source = ref_points     ##Cambiar los puntos de referencia
    dest = [(0,h),(0,0),(w,0),(w,h)]
    img = Birdseye.transformation(image,source,dest,w,h)
    return img

def inv_perspective(image):
    h = image.shape[0]
    w = image.shape[1]
    dest =  ref_points      ##Cambiar los puntos de referencia
    source = [(0,h),(0,0),(w,0),(w,h)]
    img = Birdseye.transformation(image,source,dest,w,h)
    return img

def pipeline():
    #image = "Lane Detection Test Video 01.mp4"
    cap = cv2.VideoCapture("Eurotruck_view4.mp4")
    scale_img = 0.5
    
    while cap.isOpened():
        ret, image = cap.read()

        # Check if the image was correctly captured
        if not ret:
            print("ERROR! - current frame could not be read")
            break
        
        image = cv2.resize(image, (int(image.shape[1]*scale_img), int(image.shape[0]*scale_img)))
        original_image = image
        
        ##! BLUR
        image = cv2.GaussianBlur(image, (3,3), 0)
        
        image_sobel = tf.sobelOperator(image)
        image = tf.hsvscale(image)       
        img = change_perspective(image)
        img2 = change_perspective(image_sobel)
        
        binarized = tf.threshold(img,original_image)
        
        canny = tf.cannyOperator(img2)
        
        out_img,l_c,r_c = ld.search_around_poly(binarized)
        
        out_img = inv_perspective(out_img)
        
        out_img = cv2.addWeighted(out_img, 0.3, original_image, 0.7, 0) ## Add two images
        
        out_img2,l_c2,r_c2 = ld.search_around_poly(canny)
        
        out_img2 = inv_perspective(out_img2)
        
        out_img2 = cv2.addWeighted(out_img2, 0.3, original_image, 0.7, 0) ## Add two images
        
        cv2.imshow("original", original_image)
        cv2.imshow("image", image)
        cv2.imshow("img", img)
        cv2.imshow("img2", img2)
        cv2.imshow("out_img",out_img)
        cv2.imshow("out_img2",out_img2)
        cv2.imshow("binarized",binarized)
        cv2.imshow("canny",canny)
        
        key = cv2.waitKey(10)
        if key == ord('q') or key == 27:
            print("Programm finished!")
            break
        
    cv2.destroyAllWindows()
    cap.release()
    
    return 0

if __name__ == "__main__":
    pipeline()
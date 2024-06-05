import cv2
import numpy as np
import Birdseye 
import Videoinput as vi
import transformations as tf
import laneDetection as ld

#Change perspective to birdseye
def change_perspective(image):
    h = image.shape[0]
    w = image.shape[1]
    source = [(133,465),(280,377),
              (409,385), (485,465)] ##Cambiar los puntos de referencia
    dest = [(0,h),(0,0),(w,0),(w,h)]
    img = Birdseye.transformation(image,source,dest,w,h)
    return img

def inv_perspective(image):
    h = image.shape[0]
    w = image.shape[1]
    dest =  [(133,465),(280,377),
              (409,385), (485,465)] ##Cambiar los puntos de referencia
    source = [(0,h),(0,0),(w,0),(w,h)]
    img = Birdseye.transformation(image,source,dest,w,h)
    return img

def pipeline():
    image = "Lane Detection Test Video 01.mp4"
    cap = cv2.VideoCapture(1)
    while cap.isOpened():
        ret, image = cap.read()

        # Check if the image was correctly captured
        if not ret:
            print("ERROR! - current frame could not be read")
            break
        original_image = image
        image = tf.grayscale(image)
        img = change_perspective(image)
        binarized = tf.threshold(img,original_image)
        out_img,l_c,r_c = ld.search_around_poly(binarized)
        out_img = inv_perspective(out_img)
        out_img = cv2.addWeighted(out_img, 0.3, original_image, 0.7, 0)
        cv2.imshow("img 1",out_img)
        cv2.imshow("img2",binarized)
        key = cv2.waitKey(10)
        if key == ord('q') or key == 27:
            print("Programm finished!")
            break
    cv2.destroyAllWindows()
    cap.release()
    return 0

if __name__ == "__main__":
    pipeline()
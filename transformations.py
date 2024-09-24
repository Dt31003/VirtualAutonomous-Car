import cv2
import numpy as np

#blanco_bajo = np.array([0, 0, 177])   # Valores de matiz, saturación y valor
#blanco_alto = np.array([179, 54, 255]) # Valores máximos para matiz y saturación, y valor

def hsvscale(image):
    HSV_image = cv2.cvtColor(image, cv2.COLOR_BGR2HSV)
    return HSV_image

def threshold(image,img):
    # Define el rango de colores blancos en HSV
    blanco_bajo = np.array([0, 0, 155])   # Valores de matiz, saturación y valor
    blanco_alto = np.array([179, 70, 255]) # Valores máximos para matiz y saturación, y valor

    # Crea una máscara con los colores blancos detectados
    mascara = cv2.inRange(image, blanco_bajo, blanco_alto)

    # Aplica la máscara a la imagen original}
    return mascara

def sobelOperator(img):
    ## img processing for sobel filter
    scale = 1
    delta = 0
    depth = cv2.CV_16S
    
    img_gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    
    gradient_x = cv2.Sobel(img_gray, depth, 1, 0, ksize=3, scale=scale, delta=delta, borderType=cv2.BORDER_DEFAULT)
    gradient_y = cv2.Sobel(img_gray, depth, 0, 1, ksize=3, scale=scale, delta=delta, borderType=cv2.BORDER_DEFAULT)
    
    abs_gradient_x = cv2.convertScaleAbs(gradient_x)
    abs_gradient_y = cv2.convertScaleAbs(gradient_y)
    
    gradient = cv2.addWeighted(abs_gradient_x, 0.5, abs_gradient_y, 0.5, 0)
    
    return gradient

def cannyOperator(img_gray):
    canny = cv2.Canny(img_gray, 50, 70)
    
    return canny
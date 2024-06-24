import cv2
import numpy as np

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
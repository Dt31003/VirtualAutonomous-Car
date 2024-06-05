import cv2
import numpy as np
import matplotlib.pyplot as plt

#Load image
def load_image(path):
    image = cv2.imread(path)
    return image

#Show image for test development
def show_image(img):
    cv2.imshow("Prueba",img)

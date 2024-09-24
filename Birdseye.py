import numpy as np 
import cv2 

def points(src_points,dest_poitns):
    source_points = np.array(src_points, np.float32)
    destination_points = np.array(dest_poitns, np.float32)
    return source_points, destination_points

def transformation(image,src_points,dest_poitns,width,height):
    source, destination = points(src_points,dest_poitns)
    matrix = cv2.getPerspectiveTransform(source,destination)
    img = cv2.warpPerspective(image,matrix,(width,height))
    return img

def inv_transformation(image,src_points,dest_poitns,width,height):
    source, destination = points(src_points,dest_poitns)
    matrix = cv2.getPerspectiveTransform(source,destination)
    img = cv2.warpPerspective(image,matrix,(width,height),flags=cv2.INTER_LINEAR)
    return img

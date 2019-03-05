import cv2
import time
import numpy as np
from Mod_ImageViewer import showImage

clickedPoints = []

def transformShear(image, shearFactor, direction):
    (h, w) = image.shape[:2]
    signSwitch = {
        -1: abs(h*shearFactor),
        1: 0
    }
    directionSwitch = {
        'Horizontal': horizontalShearTransformationMatrix(shearFactor, signSwitch.get(abs(shearFactor)/shearFactor), 0)
    }
    return cv2.warpAffine(image, directionSwitch.get(direction), ((int)(w + abs(h*shearFactor)), h))

def horizontalShearTransformationMatrix(factor, x_trans, y_trans):
    return np.float32([[1, factor, x_trans],[0, 1, y_trans]])

#------------------------------------------------------------------------------------------------------
#Rectifying

#Select your points in the following order: top-left, top-right, bottom-left, bottom-right
def perspectiveTransform(window, image):
    cv2.setMouseCallback(window, onClick)
    showImage(window, image)
    while(len(clickedPoints)<4):
        print('Not enough points!')
        clickedPoints.clear()
        showImage(window, image)
    (h, w) = image.shape[:2]
    oldPts = np.float32([clickedPoints[0], clickedPoints[1], clickedPoints[2], clickedPoints[3]])
    minX = np.minimum(clickedPoints[0][0], clickedPoints[2][0])
    maxX = np.maximum(clickedPoints[1][0], clickedPoints[3][0])
    minY = np.minimum(clickedPoints[0][1], clickedPoints[1][1])
    maxY = np.maximum(clickedPoints[2][1], clickedPoints[3][1])
    newPts = np.float32([[minX,minY],[maxX, minY],[minX, maxY], [maxX, maxY]])
    M = cv2.getPerspectiveTransform(oldPts, newPts)
    return cv2.warpPerspective(image, M, (w, h))

def onClick(event,x,y,flags,param):
    if(event == cv2.EVENT_LBUTTONDOWN):
        clickedPoints.append([x, y])
        #print(x, y)


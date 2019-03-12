import cv2
import numpy as np
from Mod_ImageViewer import convertToGrayscale

def getDoG(size, sigmabig, sigmasmall, angle):
    #Gaussian Kernel 1 for horizontal image smoothing
    gaussian1DHorizontal = np.array(cv2.getGaussianKernel(size, sigmabig))
    #Gaussian Kernel 2 for vertical image smoothing
    gaussian1DVertical = np.transpose(cv2.getGaussianKernel(size, sigmasmall))
    matrix = np.zeros((size, size))
    matrix[:, (int(size/2)):(int(size/2))+1] = np.array(gaussian1DHorizontal)
    #Basic DoG = difference between the two smoothed images to detect edges
    gaussian2D = cv2.filter2D(matrix, -1, gaussian1DVertical)
    #Sobel for horizontal edge detection
    gaussian2D = cv2.Sobel(gaussian2D, -1, 1, 0, 3)
    #Rotation matrix to slightly change the direction of edge detection
    rotMatrix = cv2.getRotationMatrix2D(((int(size/2)),(int(size/2))), angle, 1)
    DoGKernel = cv2.warpAffine(gaussian2D, rotMatrix, (size,size))
    return DoGKernel

def visualiseDoG(kernel):
    min_val, max_val, min_loc, max_loc = cv2.minMaxLoc(kernel)
    result = (kernel * (0.5)/max_val) + 0.5
    return result

def findEdges(image, angle):
    result = convertToGrayscale(image)
    result = cv2.convertScaleAbs(cv2.filter2D(result, cv2.CV_32F, getDoG(75,25,1,angle)))
    return result

def findEdgesWithThreshold(image, angle):
    (retval, result) = cv2.threshold(findEdges(image,angle),100,255,cv2.THRESH_BINARY)
    return result


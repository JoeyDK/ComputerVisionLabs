import cv2
import numpy as np

#Gaussian Blur
def gaussianBlur(image, gaussianKernelSizeWidth, gaussianKernelSizeHeight, sigma):
    return cv2.GaussianBlur(image,(gaussianKernelSizeWidth, gaussianKernelSizeHeight), sigma,cv2.BORDER_DEFAULT)

#Median Blur
def medianBlur(image, medianKernelSize):
    return cv2.medianBlur(image, medianKernelSize)

#Sharpen Image
def sharpen(image):
    blurredImage = gaussianBlur(image, 3, 3, 7)
    #Increase both factors to increase sharpness
    result = cv2.addWeighted(image, 8, blurredImage, -7, 0)
    return result

#Sobel gradient
def sobelGradient(image, dx, dy):
    #Sobel(src, ddepth, order_x, order_y, kernelsize)
    #order_x=1 & order_y=0 => horizontal gradient
    #order_x=0 & order_y=1 => vertical gradient
    #Use CV_16S to support both positive & negative values of the sobel result
    #Convert back to absolute values to change negatives to positives
    return cv2.convertScaleAbs(cv2.Sobel(image, cv2.CV_16S, dx, dy, 3, 1))

#Sobel gradients put together
def sobelFull(image):
    sobelx = sobelGradient(image, 1, 0)
    sobely = sobelGradient(image, 0, 1)
    #Not exact calculation (the correct one is sqrt(sobelx² + sobely²))
    return cv2.addWeighted(sobelx, 0.5, sobely, 0.5, 0)

#Custom kernel filter
def customFilter(image, kernel):
    return cv2.filter2D(image, -1, np.asarray(kernel), (len(kernel)-1, len(kernel)-1))
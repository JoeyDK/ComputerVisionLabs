import cv2
#import numpy as np  ->  only used if we modify pixels manually

#Read image from filename
def readImage(filename):
    return cv2.imread(filename)

def writeImage(filename, image):
    cv2.imwrite(filename, image)
    return

#Show an image and destroy after key press
def showImage(imagename, image):
    cv2.imshow(imagename, image)
    cv2.waitKey(0)
    return

def showDoubleImage(imagename1, imagename2, image1, image2):
    cv2.imshow(imagename1,image1)
    cv2.imshow(imagename2, image2)
    cv2.waitKey(0)
    return

#Convert an image to grayscale
def convertToGrayscale(image):
    return cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

#Create a binary image with given factor as threshold percentage
def thresholdGrayscale(imageIn, thresholdFactor):
    retval, imageOut = cv2.threshold(imageIn, round(thresholdFactor*255), 255, cv2.THRESH_BINARY)
    return imageOut

#Define the window to view the images
def start(windowName):
    cv2.namedWindow(windowName, flags=cv2.WINDOW_AUTOSIZE)

#Destroy all created windows
def end():
    cv2.destroyAllWindows()
    return



import cv2
import numpy as np
import math
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

#----------------------------------------------------------------------------------------------------------------------

def findAllEdges(image, min_thres, max_thres):
    return cv2.Canny(convertToGrayscale(image), min_thres, max_thres, None, 5, True)

def showAllLines(image):
    edges = findAllEdges(image, 50, 200)
    result = image.copy()
    lines = cv2.HoughLines(edges, 1, np.pi/180, 110, None, 0, 0)
    if lines is not None:
        for i in range(0, len(lines)):
            rho = lines[i][0][0]
            theta = lines[i][0][1]
            a = math.cos(theta)
            b = math.sin(theta)
            x0 = a*rho
            y0 = b*rho
            pt1 = (int(x0 + 1000*(-b)), int(y0 + 1000*(a)))
            pt2 = (int(x0 - 1000*(-b)), int(y0 - 1000*(a)))
            cv2.line(result, pt1, pt2, (0,0,0), 2, cv2.LINE_AA)
    return result

def showAllCorners(image):
    result = image.copy()
    corners = cv2.goodFeaturesToTrack(convertToGrayscale(image), 100, 0.2, 8)
    if corners is not None:
        for point in corners:
            x = point[0][0]
            y = point[0][1]
            cv2.circle(result, (x,y), 8, (0,0,255), 1)
    return result

#----------------------------------------------------------------------------------------------------------------------

def getORBFeatures(image, amountOfFeatures):
    orb = cv2.ORB_create(nfeatures=amountOfFeatures)
    keypoints, descriptors = orb.detectAndCompute(image, None)
    return (keypoints, descriptors)

def drawORBFeatures(image, amountOfFeatures):
    keypoints, descriptors = getORBFeatures(image, amountOfFeatures)
    result = image.copy()
    if keypoints is not None:
        for kp in keypoints:
            x = int(kp.pt[0])
            y = int(kp.pt[1])
            cv2.circle(result, (x, y), 8, (0, 0, 255), 1)
    return result

def matchORBFeatures(descriptors1, descriptors2, amountOfMatches):
    bf = cv2.BFMatcher_create(cv2.NORM_HAMMING, crossCheck=True)
    matches = bf.match(descriptors1, descriptors2)
    matches = sorted(matches, key = lambda x:x.distance)
    return matches[:amountOfMatches]

def drawORBMatches(image1, image2, amountOfFeatures, amountOfMatches):
    kps1, des1 = getORBFeatures(image1, amountOfFeatures)
    kps2, des2 = getORBFeatures(image2, amountOfFeatures)
    matches = matchORBFeatures(des1, des2, amountOfMatches)
    result = cv2.drawMatches(image1, kps1, image2, kps2, matches, None, matchColor=(0,0,255), flags=2)
    return result
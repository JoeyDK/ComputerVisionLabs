import cv2
import numpy as np
import math
from Mod_ImageViewer import convertToGrayscale
from Mod_FeatureDetection import getDoG

def getDoGFilters():
    DoGFilters = np.empty(12, dtype=object)
    for i in range(1,3):
        for j in range(6):
            DoGFilters[(i-1)*6+j] = getDoG(10*(i)+1, 4*i+5, 1, j*30 - 90)
    return DoGFilters

def filterWithDoG(image, kernel):
    result = convertToGrayscale(image)
    result = cv2.convertScaleAbs(cv2.filter2D(result, cv2.CV_32F, kernel))
    return result

def getFilteredImages(image):
    vectors = np.empty(12, dtype=object)
    kernels = getDoGFilters()
    for i in range(12):
        vectors[i] = filterWithDoG(image, kernels[i])
    return vectors

def getFeatureBlocks(image):
    filteredImages = getFilteredImages(image)
    (h,w) = image.shape[:2]
    x_blocks = math.ceil(w/16)
    y_blocks = math.ceil(h/16)
    featureBlocks = np.empty([x_blocks,y_blocks,len(filteredImages)], dtype=object)
    for i in range(x_blocks):
        for j in range(y_blocks):
            for k in range(len(filteredImages)):
                max_val = (abs(filteredImages[k][j*16:min((j+1)*16,h), i*16:min((i+1)*16,w)])).max()
                featureBlocks[i][j][k] = max_val
    return featureBlocks

def getMeanFeatureVectorValues(image, vectorImage):
    (h, w) = image.shape[:2]
    featureblocks = getFeatureBlocks(image)
    (x_blocks, y_blocks, featureAmount) = featureblocks.shape[:3]
    meanFeatureVectorValues = np.zeros([2,12], dtype=object)
    for k in range(featureAmount):
        positive_blocks = 0
        negative_blocks = 0
        for i in range(x_blocks):
            for j in range(y_blocks):
                #print(str(j)+"/"+str(i)+": "+str(vectorImage[j*16][i*16]))
                if(vectorImage[j*16+8][i*16+8] == 255):
                    positive_blocks += 1
                    meanFeatureVectorValues[0][k] += featureblocks[i][j][k]
                else:
                    negative_blocks += 1
                    meanFeatureVectorValues[1][k] += featureblocks[i][j][k]
        if(positive_blocks != 0):
            meanFeatureVectorValues[0][k] /= positive_blocks
        if(negative_blocks != 0):
            meanFeatureVectorValues[1][k] /= negative_blocks
    return meanFeatureVectorValues
import cv2
import math
import numpy as np
import pandas as pd
from sklearn.ensemble import RandomForestClassifier
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

#--------------------------------------------------------------------------------

def createFeatureVectors(images):
    amount = len(images)
    featureVectors = np.empty(amount, dtype=object)
    for i in range(amount):
        featureVectors[i] = getFeatureBlocks(images[i])
    return featureVectors

def createDataSet(images, vectorImages, items):
    if(len(images)!=len(vectorImages)):
        return None
    featureVectors = createFeatureVectors(images)
    (x, y, amount) = featureVectors[0].shape[:3]
    dataset = np.empty([2*items*len(vectorImages), amount+1], dtype=object)
    for l in range(len(vectorImages)):
        positives = []
        negatives = []
        for i in range(x):
            for j in range(y):
                if(vectorImages[l][j*16+8][i*16+8] == 255):
                    positives.append([i,j])
                else:
                    negatives.append([i,j])
        for p in range(items):
            for am in range(amount):
                (rand_x, rand_y) = positives[np.random.randint(len(positives))]
                dataset[l*2*items+p][am] = featureVectors[l][rand_x][rand_y][am]
            dataset[l*2*items+p][amount] = "road"
        for n in range(items):
            for am in range(amount):
                (rand_x, rand_y) = negatives[np.random.randint(len(negatives))]
                dataset[l*2*items+items+n][am] = featureVectors[l][rand_x][rand_y][am]
            dataset[l*2*items+items+n][amount] = "non-road"
    col = []
    for am in range(amount):
        col.append('index '+str(am))
    col.append('type')
    result = pd.DataFrame(dataset, columns=col)
    return result

def trainRDF(dataset):
    features = dataset.columns[:12]
    y = pd.factorize(dataset['type'])[0]
    rdf = RandomForestClassifier(n_jobs=2, random_state=0, n_estimators=10, min_samples_leaf=5)
    rdf.fit(dataset[features], y)
    return rdf

def createPrediction(image, rdf):
    overlay = image.copy()
    (h,w) = overlay.shape[:2]
    featureblocks = getFeatureBlocks(image)
    (x, y, amount) = featureblocks.shape[:3]
    col = []
    for am in range(amount):
        col.append('index ' + str(am))
    for i in range(x):
        for j in range(y):
            testset = pd.DataFrame([featureblocks[i][j]], columns=col)
            features = testset.columns[:12]
            prediction = rdf.predict(testset[features])
            overlay[j*16:min((j+1)*16,h), i*16:min((i+1)*16,w)] = ((1-prediction[0])*0, (prediction[0])*255, (1-prediction[0])*255)
            print("("+str(i)+","+str(j)+"): "+str(prediction))
    result = cv2.addWeighted(image, 0.4, overlay, 0.1, 0)
    return result

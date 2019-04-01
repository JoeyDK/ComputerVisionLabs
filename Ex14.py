import sys

from Mod_ImageViewer import *
from Mod_Classification import *
from Mod_FeatureDetection import visualiseDoG

#EX 14 -----------------------------------------------------
if(len(sys.argv)>2):

    filename = sys.argv[1]
    vectorfilename = sys.argv[2]
    windowname1 = 'DoG filters'

    image = readImage(filename)
    vectorImage = readImage(vectorfilename)

    filters = getDoGFilters()
    vectors = getFilteredImages(image)
    values = getMeanFeatureVectorValues(image, convertToGrayscale(vectorImage))

    start(windowname1)
    for filter in filters:
        showImage(windowname1, visualiseDoG(filter))
    for vector in vectors:
        showImage(windowname1, vector)
    print("Road mark block values: ")
    for index in range(len(values[0])):
        print("Position" + str(index) + ": " + str(values[0][index]))
    print('\n')
    print("Non-road mark block values: ")
    for index in range(len(values[1])):
        print("Position" + str(index) + ": " + str(values[1][index]))
    print('\n')
    end()

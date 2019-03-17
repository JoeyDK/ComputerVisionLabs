import sys

from Mod_ImageViewer import *
from Mod_FeatureDetection import *

#EX 13 -----------------------------------------------------
if(len(sys.argv)>2):
    filename1 = sys.argv[1]
    filename2 = sys.argv[2]

    windowname1 = 'image 1'
    windowname2 = 'image 2'
    windowname3 = 'matches'

    image1 = readImage(filename1)
    image2 = readImage(filename2)
    image3 = drawORBFeatures(image1, 98)
    image4 = drawORBFeatures(image2, 98)
    image5 = drawORBMatches(image1, image2, 98, 48)

    start(windowname1)
    start(windowname2)
    showDoubleImage(windowname1, windowname2, image3, image4)
    end()
    start(windowname3)
    showImage(windowname3, image5)

    writeImage('ImageResults/EX13_ResultImage1.png', image3)
    writeImage('ImageResults/EX13_ResultImage2.png', image4)
    writeImage('ImageResults/EX13_Matches.png', image5)
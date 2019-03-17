import sys

from Mod_ImageViewer import *
from Mod_FeatureDetection import *

#EX 11 -----------------------------------------------------
if(len(sys.argv)>1):
    filename = sys.argv[1]

    windowname1 = 'original window'
    windowname2 = 'edges window'
    windowname3 = 'lines window'

    image1 = readImage(filename)
    image2 = findAllEdges(image1, 50, 200)
    image3 = showAllLines(image1)

    start(windowname1)
    start(windowname2)
    showDoubleImage(windowname1, windowname2, image1, image2)
    end()
    start(windowname3)
    showDoubleImage(windowname1, windowname3, image1, image3)

    writeImage('ImageResults/EX11_Result(Canny).png', image2)
    writeImage('ImageResults/EX11_Result(Hough).png', image3)
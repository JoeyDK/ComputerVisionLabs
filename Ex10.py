import sys

from Mod_ImageViewer import *
from Mod_EdgeDetection import *

#EX 10 -----------------------------------------------------
if(len(sys.argv)>1):
    filename = sys.argv[1]

    windowname1 = 'original window'
    windowname2 = 'yellow edges window'
    windowname3 = 'yellow edges window (after threshold)'

    image1 = readImage(filename)
    image2 = findEdges(image1, -15)
    image3 = findEdgesWithThreshold(image1, -15)

    start(windowname1)
    start(windowname2)
    showDoubleImage(windowname1, windowname2, image1, image2)
    end()
    showDoubleImage(windowname1, windowname3, image1, image3)
    end()

    writeImage('ImageResults/EX10_Result.png', image2)
    writeImage('ImageResults/EX10_Result(threshold).png', image3)
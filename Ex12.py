import sys

from Mod_ImageViewer import *
from Mod_EdgeDetection import *

#EX 12 -----------------------------------------------------
if(len(sys.argv)>2):
    filename1 = sys.argv[1]
    filename2 = sys.argv[2]

    windowname1 = 'image 1'
    windowname2 = 'image 2'

    image1 = readImage(filename1)
    image2 = readImage(filename2)
    image3 = showAllCorners(image1)
    image4 = showAllCorners(image2)

    start(windowname1)
    start(windowname2)
    showDoubleImage(windowname1, windowname2, image3, image4)
    end()

    writeImage('ImageResults/EX12_ResultImage1.png', image3)
    writeImage('ImageResults/EX12_ResultImage2.png', image4)
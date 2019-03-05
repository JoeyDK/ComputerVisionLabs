import sys

from Mod_ImageViewer import *
from Mod_Transformations import *

#EX 9 -----------------------------------------------------
if(len(sys.argv)>1):
    filename = sys.argv[1]

    windowname1 = 'original window'
    windowname2 = 'rectified window'

    start(windowname1)
    image1 = readImage(filename)
    image2 = perspectiveTransform(windowname1, image1)

    start(windowname2)
    showDoubleImage(windowname1, windowname2, image1, image2)
    writeImage('ImageResults/EX9_Result.png', image2)

    end()
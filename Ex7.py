import sys

from Mod_ImageViewer import *
from Mod_Morphologicals import *

#EX 7 -----------------------------------------------------
if(len(sys.argv)>1):
    filename = sys.argv[1]

    windowname1 = 'original window'
    windowname2 = 'morphed window'

    start(windowname1)
    start(windowname2)

    image1 = readImage(filename)
    image2 = erode(image1, 'Rectangle', 10, 1, 1)
    image2 = dilate(image2, 'Rectangle', 3, 14, 1)

    writeImage('ImageResults/EX7_Result.png', image2)

    showDoubleImage(windowname1, windowname2, image1, image2)

    end()
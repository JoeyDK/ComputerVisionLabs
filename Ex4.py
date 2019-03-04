import sys

from Mod_ImageViewer import *
from Mod_Filters import medianBlur

#EX 4 -----------------------------------------------------
if(len(sys.argv)>1):
    filename = sys.argv[1]
    windowname1 = 'regular window'
    windowname2 = 'filtered window'

    start(windowname1)
    start(windowname2)

    image1 = readImage(filename)
    image2 = medianBlur(image1, 5)

    showDoubleImage(windowname1, windowname2, image1, image2)

    writeImage('ImageResults/EX4_Result.png', image2)

    end()
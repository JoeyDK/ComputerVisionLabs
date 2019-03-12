import sys

from Mod_ImageViewer import *
from Mod_Filters import *

#EX 6 -----------------------------------------------------
if(len(sys.argv)>1):
    filename = sys.argv[1]

    kernel = [[0 for x in range(15)] for y in range(15)]
    for i in range(7):
        kernel[i][i] = 1/7

    windowname1 = 'original window'
    windowname2 = 'filtered window'

    start(windowname1)
    start(windowname2)

    image1 = readImage(filename)
    image2 = customFilter(image1, kernel)

    showDoubleImage(windowname1, windowname2, image1, image2)

    writeImage('ImageResults/EX6_Result.png', image2)

    end()
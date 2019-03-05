import sys

from Mod_ImageViewer import *
from Mod_Transformations import *

#EX 8 -----------------------------------------------------
if(len(sys.argv)>1):
    filename = sys.argv[1]

    windowname1 = 'original window'
    windowname2 = 'sheared window right'
    windowname3 = 'sheared window left'

    image1 = readImage(filename)
    image2 = transformShear(image1, -0.2, 'Horizontal')
    image3 = transformShear(image1, 0.2, 'Horizontal')

    start(windowname1)
    start(windowname2)
    showDoubleImage(windowname1, windowname2, image1, image2)
    writeImage('ImageResults/EX8_Result.png', image2)
    end()

    start(windowname1)
    start(windowname3)
    showDoubleImage(windowname1, windowname3, image1, image3)
    end()
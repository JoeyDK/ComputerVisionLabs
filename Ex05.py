import sys

from Mod_ImageViewer import *
from Mod_Filters import *

#EX 5 -----------------------------------------------------
if(len(sys.argv)>1):
    filename = sys.argv[1]
    windowname1 = 'gradient x window'
    windowname2 = 'gradient y window'

    image1 = convertToGrayscale(readImage(filename))
    imagex = sobelGradient(image1, 1, 0)
    imagey = sobelGradient(image1, 0, 1)

    showDoubleImage(windowname1, windowname2, imagex, imagey)

    end()

    windowname3 = 'total gradient'
    imageTotal = sobelFull(image1)

    showImage(windowname3, imageTotal)

    writeImage('ImageResults/EX5_Result_x.png', imagex)
    writeImage('ImageResults/EX5_Result_y.png', imagey)
    writeImage('ImageResults/EX5_Result_total.png', imageTotal)

    end()
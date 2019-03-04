from Mod_ImageViewer import *
import sys

if(len(sys.argv)>1):
    filename = sys.argv[1]
    windowname = "Cloud Image"
    start(windowname)
    image = readImage(filename)
    showImage(windowname, image)
    image = convertToGrayscale(image)
    writeImage("ImageResults/EX1_grayscaled.png", image)
    showImage(windowname, image)
    image2 = thresholdGrayscale(image, 0.5)
    writeImage("ImageResults/EX1_thresholded.png", image2)
    showImage(windowname, image2)
    end()
import cv2

from Mod_ImageViewer import *
from Mod_FeatureDetection import *

#EX 10b -----------------------------------------------------
windowname1 = 'DoG visualising window'

image1 = visualiseDoG(getDoG(75, 25, 1, -15))
image1 = cv2.resize(image1, (500, 500))

start(windowname1)
showImage(windowname1, image1)
writeImage("ImageResults/EX10_Kernel.png", image1*255.0)
end()
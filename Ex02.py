from Mod_ImageViewer import *
from Mod_Filters import gaussianBlur

#EX 2 -----------------------------------------------------
windowname1 = 'regular window'
windowname2 = 'blurred window'
start(windowname1)
start(windowname2)

image1 = readImage('Images/whitenoise.png')
image2 = gaussianBlur(image1, 0, 0, 3)

showDoubleImage(windowname1, windowname2, image1, image2)

writeImage('ImageResults/EX2_Result.png', image2)

end()
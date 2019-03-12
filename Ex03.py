from Mod_ImageViewer import *
from Mod_Filters import sharpen

#EX 3 -----------------------------------------------------
windowname1 = 'regular window'
windowname2 = 'sharpening window'
start(windowname1)
start(windowname2)

image1 = readImage('Images/unsharp.png')
image2 = sharpen(image1)

showDoubleImage(windowname1, windowname2, image1, image2)

writeImage('ImageResults/EX3_Result.png', image2)

end()
import sys

from Mod_ImageViewer import *
from Mod_Classification import *

#EX 15 -----------------------------------------------------
if(len(sys.argv)>4):

    file1 = str(sys.argv[1])
    file2 = str(sys.argv[2])
    file3 = str(sys.argv[3])
    file4 = str(sys.argv[4])

    windowname1 = "Image with features"

    image1 = readImage("Images/"+file1+".png")
    image2 = readImage("Images/"+file2+".png")
    image3 = readImage("Images/"+file3+".png")
    image4 = readImage("Images/"+file4+".png")
    vector1 = convertToGrayscale(readImage("Images/"+file1+"_blocks.png"))
    vector2 = convertToGrayscale(readImage("Images/"+file2+"_blocks.png"))
    vector3 = convertToGrayscale(readImage("Images/"+file3+"_blocks.png"))
    vector4 = convertToGrayscale(readImage("Images/"+file4+"_blocks.png"))

    images = [image1, image2, image3, image4]
    vectors = [vector1, vector2, vector3, vector4]

    dataset = createDataSet(images, vectors, 20)
    predictor = trainRDF(dataset)
    #print(dataset.head())
    resultImage1 = createPrediction(image1, predictor)
    resultImage2 = createPrediction(image2, predictor)
    resultImage3 = createPrediction(image3, predictor)
    resultImage4 = createPrediction(image4, predictor)

    showImage(windowname1, resultImage1)
    showImage(windowname1, resultImage2)
    showImage(windowname1, resultImage3)
    showImage(windowname1, resultImage4)

    writeImage("ImageResults/EX15_Result1.png", resultImage1)
    writeImage("ImageResults/EX15_Result2.png", resultImage2)
    writeImage("ImageResults/EX15_Result3.png", resultImage3)
    writeImage("ImageResults/EX15_Result4.png", resultImage4)

    end()

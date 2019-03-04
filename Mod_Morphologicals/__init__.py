import cv2

def erode(image, kernelType, x, y, it):
    switcher = {
        'Rectangle': rectangularKernel(x,y),
        'Ellipse': ellipticalKernel(x,y)
        }
    return cv2.erode(image, switcher.get(kernelType), iterations = it)

def dilate(image, kernelType, x, y, it):
    switcher = {
        'Rectangle': rectangularKernel(x, y),
        'Ellipse': ellipticalKernel(x, y)
    }
    return cv2.dilate(image, switcher.get(kernelType), iterations = it)

def rectangularKernel(x, y):
    return cv2.getStructuringElement(cv2.MORPH_RECT, (x,y))

def ellipticalKernel(x, y):
    return cv2.getStructuringElement(cv2.MORPH_ELLIPSE, (x,y))
import cv2 as cv
import numpy as np

img = cv.imread('photos/sky.JPG')
cv.imshow('sky', img)

def translate(img, x,y):
    transMat = np.float32([[1,0,x],[0,1,y]])
    dimensions = (img.shape[1], img.shape[0])
    return cv.warpAffine(img, transMat, dimensions)
# -x --> left
# -y --> up
# x ---> right
# y--> down

translated = translate(img, 100,100)
cv.imshow('translated', translated)

#rotating an img
def rotate(img, angle, rotPoint = None):
    (height,width) = img.shape[:2]

    if rotPoint is None:
        rotPoint =(width//2, height// 2)
    rotMat = cv.getRotationMatrix2D(rotPoint, angle, 1.0)
    dimensions= (width,height)

    return cv.warpAffine(img, rotMat, dimensions)

rotated = rotate(img, 45)
cv.imshow('rotated', rotated)

rotated_rotated= rotate(rotated, -45)
cv.imshow('rotate2', rotated_rotated)

#flipping flip codes
flip = cv.flip(img, 0 )
cv.imshow('flipped', flip)

cv.waitKey(0)
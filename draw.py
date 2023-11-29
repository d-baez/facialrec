import cv2 as cv
import numpy as np

# create blank canvas
blank = np.zeros((500,500,3), dtype='uint8')
cv.imshow('blank',blank)
# paint image a certain color
blank[200:300,300:400] = 0,0,255
cv.imshow('red box', blank)

# img = cv.imread('photos/sky.JPG')
# cv.imshow('img', img)

# draw a circle
cv.circle(blank,(250,250), 40, (0,255,0),thickness=3)
cv.imshow('circle',blank)

# print text
cv.putText(blank, 'hello world', (255,255), cv.FONT_HERSHEY_PLAIN, 1.0,[0,0,230], 2)
cv.imshow('Text',blank)

cv.waitKey(0)

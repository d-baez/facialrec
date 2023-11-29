import cv2 as cv

img = cv.imread('photos/crowd.Jpeg')
cv.imshow('img', img)
# grayscale
gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)
cv.imshow('gray', gray)

#canny
canny = cv.Canny(img, 125, 175)
cv.imshow('canny edge', canny)

#contours
countours, hiearchies = cv.findContours(canny, cv.RETR_LIST, cv.CHAIN_APPROX_SIMPLE)





cv.waitKey(0)



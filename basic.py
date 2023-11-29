import cv2 as cv
img = cv.imread('photos/faces2.JPG')
cv.imshow('group photo', img)

#converting to grayscale
gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)
cv.imshow('gray',gray)

#blur image / increase ksize to blur more
blur = cv.GaussianBlur(img, (7,7), cv.BORDER_DEFAULT)
cv.imshow('blur', blur)

#edge cascade
canny= cv.Canny( img, 125, 175)
cv.imshow('edge', canny)

#dilating the image
dilated = cv.dilate(canny, (7,75), iterations=3)
cv.imshow('dialated', dilated)

#eroding
eroded = cv.erode(dilated,(7,7), iterations=3)
cv.imshow('Eroded',eroded)

#resize
resized = cv.resize(img, (500,500), interpolation=cv.INTER_CUBIC)
cv.imshow('resized', resized)

#croped
cropped = img[50:200, 150:400]
cv.imshow('cropped', cropped)


cv.waitKey(0)
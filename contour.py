import cv2 as cv

img = cv.imread('photos/crowd.Jpeg')
cv.imshow('img', img)
# grayscale
gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)
cv.imshow('gray', gray)

blur = cv.GaussianBlur(gray,(5,5), cv.BORDER_DEFAULT)
cv.imshow('blur',blur)

#canny
canny = cv.Canny(blur, 125, 175)
cv.imshow('canny edge', canny)

#contours
countours, hiearchies = cv.findContours(canny, cv.RETR_LIST, cv.CHAIN_APPROX_SIMPLE)
print(f'{len(countours)} countors found')




cv.waitKey(0)



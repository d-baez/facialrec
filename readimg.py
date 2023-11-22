import cv2 as cv
#  take a photo file from /photos
img = cv.imread('photos/faces.JPG')
# assign image file to img

cv.imshow('brazil', img)
# imshow (' window name' , file)



cv.waitKey(0)
# wait until a key is pressed to close
# todo test code to make sure all packages work

import cv2 as cv
#reading videos must start cap, capture (0) refrence webcam
cap = cv.VideoCapture('videos/IMG_5275.MOV')

def rescaleFrame( frame, scale = .75):
    width = int(frame.shape[1] *scale)
    height = int (frame.shape[0] *scale)
    dimensions = (width, height)
    return cv.resize(frame,dimensions,cv.INTER_AREA)



# read video frame by frame
while True:
    isTrue, frame = cap.read()
    frame_resized = rescaleFrame(frame)

    #display video
    cv.imshow("video", frame)
    cv.imshow('resizedVid', frame_resized)

    if cv.waitKey(20) & 0xFF==ord('d'):
        break
cap.release
cv.destroyAllWindows()





cv.waitKey(0)
import numpy as np
import cv2

# capture video
cap = cv2.VideoCapture(1)
#descripe a loop
#read video frame by frame
while True:
    ret,img = cap.read()
    cv2.imshow('Original Video',img)
    #flip for truning(fliping) frames of video
    img2=cv2.flip(img,-1)
    cv2.imshow('Flipped video',img2)
    k=cv2.waitKey(30) & 0xff
    #once you inter Esc capturing will stop
    if k==27:
        break
    cap.release()
    cv2.destroyAllWindows()
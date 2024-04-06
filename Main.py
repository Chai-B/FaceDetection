import cv2 as cv
import sys

face_cascade = cv.CascadeClassifier('/Users/chaitanyabansal/Desktop/python/face detection/facedetector.xml')
eye_cascade= cv.CascadeClassifier('/Users/chaitanyabansal/Desktop/python/face detection/eyedetector.xml')
#img=cv.imread('/Users/chaitanyabansal/Desktop/python/face detection/img.jpeg')
#if img is None:
    #sys.exit("Could not read the image.")
#gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY) 

#cv.imshow("new", img)
#k = cv.waitKey(3000)

cap = cv.VideoCapture(0)
while(True):
    ret, frame = cap.read() 
    gray = cv.cvtColor(frame, cv.COLOR_BGR2GRAY) 
    faces = face_cascade.detectMultiScale(gray, 1.2, 7) 
    for (x, y, w, h) in faces:
        cv.rectangle(frame, (x, y), (x + w, y + h), (0, 255, 0), 2)
        roi_gray = gray[y:y+h, x:x+w] 
        roi_color = frame[y:y+h, x:x+w] 
        eyes = eye_cascade.detectMultiScale(roi_gray,1.2,5)
        for (ex,ey,ew,eh) in eyes: 
            cv.rectangle(roi_color,(ex,ey),(ex+ew,ey+eh),(0,127,255),2)
    cv.imshow('frame',frame)
    if cv.waitKey(1) & 0xFF == ord('q'):
        break
cap.release() 

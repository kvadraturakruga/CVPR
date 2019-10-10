import cv2
import numpy as np 

key = cv2. waitKey(1)
webcam = cv2.VideoCapture(0)
while True:    
    check, frame = webcam.read()
    cv2.imshow("Capturing", frame)
    key = cv2.waitKey(1)
    if key == ord('s'): 
        cv2.imwrite(filename='original_frame.jpg', img=frame)
        webcam.release()
        cv2.waitKey(3450)
        cv2.destroyAllWindows()
        break
    elif key == ord('q'):
        print("Turning off camera.")
        webcam.release()
        cv2.destroyAllWindows()
        break
    
image = cv2.imread('original_frame.jpg')
gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
gray_background = cv2.cvtColor(gray, cv2.COLOR_GRAY2BGR)

cv2.line(gray_background, (0,0), (640,480), (0, 0, 255), thickness=3, lineType=8)
cv2.rectangle(gray_background,(0,0),(134,78),(255,0,0),3) 

cv2.imshow('Original image',image)
cv2.imshow('Gray image', gray_background)
  
cv2.waitKey(0)
cv2.destroyAllWindows()
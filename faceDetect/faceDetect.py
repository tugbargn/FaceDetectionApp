# Importing OpenCV package
import cv2
#import matplotlib.pyplot as plt

try:
    # Reading the image
    #img = cv2.imread('../input/facephotos/photo2.jpeg')
    img = cv2.imread('test.jpg')
    # Converting image to grayscale
    gray_img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

    # Loading the required haar-cascade xml classifier file
    haar_cascade = cv2.CascadeClassifier('haarcascades/haarcascade_frontalface_default.xml')
    eye_cascade = cv2.CascadeClassifier('haarcascades/haarcascade_eye.xml')

    # Applying the face detection method on the grayscale image
    faces_rect = haar_cascade.detectMultiScale(gray_img, 1.1, 9)

    faceCounter = 0
    # Iterating through rectangles of detected faces
    for (x, y, w, h) in faces_rect:
        cv2.rectangle(img, (x, y), (x+w, y+h), (0, 255, 0), 2)
        faceCounter += 1

    cv2.namedWindow("test", cv2.WINDOW_NORMAL)
    cv2.resizeWindow("test", 400, 600)
    cv2.imshow("test", img)
    
    if faceCounter > 0:
        print("number of faces: ", faceCounter)
    else:
        print("No face detected!")

except:
    print("An error occured above!")

cv2.waitKey(0)
cv2.destroyAllWindows()

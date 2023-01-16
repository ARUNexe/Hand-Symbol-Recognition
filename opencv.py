import cv2
import mediapipe as mp
from cvzone.HandTrackingModule import HandDetector
import time

detector = HandDetector(maxHands=1)

#training data folder
folder = "Data/Super"
counter=0

cap = cv2.VideoCapture(0)
while True:
    data, image = cap.read()
    hands, image = detector.findHands(image)

    if hands:
        hand = hands[0]
        x,y,w,h = hand['bbox']

        imgcroped = image[y-15:y + h+15,x-15:x + w+15]
        try:
            imgcroped = cv2.resize(imgcroped,(300,300))
            cv2.imshow('HandsCroped', imgcroped)
        except:
            print("hand out of image")





    cv2.imshow('Hands', image)
    key = cv2.waitKey(1)

    #press "s" for taking a picture of hand
    if key == ord("s"):
        counter += 1
        print(counter)
        cv2.imwrite(f'{folder}/Image_{time.time()}.jpg',imgcroped)

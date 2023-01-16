import cv2
import mediapipe as mp
from cvzone.HandTrackingModule import HandDetector
from cvzone.ClassificationModule import Classifier
import time
detector = HandDetector(maxHands=1)
classifier = Classifier("models/keras_ml_model.h5","models/labels.txt")

lables = ["None","Peace","Fuck you","Thumps up","Super"]
cap = cv2.VideoCapture(0)

while True:
    data, image = cap.read()
    hands, image = detector.findHands(image)
    imageOutput = image.copy()
    if hands:
        hand = hands[0]
        x,y,w,h = hand['bbox']
        imgcroped = image[y-15:y + h+15,x-15:x + w+15]
        try:
            imgcroped = cv2.resize(imgcroped,(300,300))
            cv2.imshow('HandsCroped', imgcroped)
            prediction, index = classifier.getPrediction(imgcroped)
            print(prediction, lables[index])
        except:
            print("hand out of image")




        cv2.putText(imageOutput,lables[index],(x,y-20),cv2.FONT_HERSHEY_COMPLEX,1,(0,0,0),1)

    cv2.imshow('Hands', imageOutput)
    cv2.waitKey(1)



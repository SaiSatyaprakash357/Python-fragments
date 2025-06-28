from cvzone.HandTrackingModule import HandDetector
from cvzone.Utils import putTextRect
import cv2
import time
import os

cap = cv2.VideoCapture(0)

detector = HandDetector(staticMode=False, maxHands=1, modelComplexity=1, detectionCon=0.5, minTrackCon=0.5)

prev_fingers = []
gesture = 0
ges_complete = False
gesture_sequence = [[0, 1, 1, 1, 0], 
                    [0, 1, 1, 0, 0], 
                    [0, 1, 0, 0, 0], 
                    [0, 0, 0, 0, 0]]

def addText (img) : 
     img, bbox = putTextRect(
            img, 
            "OYASUMI", 
            (400, 100), 
            scale=1, 
            thickness=2, 
            colorT=(255, 0, 0), 
            colorR=(0, 255, 0),
            colorB=(0, 0, 255),
            font=cv2.FONT_HERSHEY_SIMPLEX, 
            offset=10, 
            border=3
        )
     return img

while True:
    success, img = cap.read()
    img = cv2.resize(img, (960, 720))
    hand, img = detector.findHands(img, draw=True, flipType=True)

    if hand:
        hand = hand[0] 
        lmList = hand["lmList"] 
        bbox = hand["bbox"] 
        center = hand['center'] 
        handType = hand["type"]

        new_fingers = detector.fingersUp(hand)
        if new_fingers != prev_fingers :
            print(f"{handType} Hand = {new_fingers}")
            prev_fingers = new_fingers

            if new_fingers == gesture_sequence[gesture] :
                 gesture += 1
            else :
                 gesture = 0

        if gesture == len(gesture_sequence) :
             gesture = 0
             ges_complete = True
             start_time = time.time()  
            
        if ges_complete :
             if time.time() - start_time < 2 :
                  img = addText(img)
             elif time.time() - start_time > 2 :
                  os.system("taskkill /f /im Code.exe")
        
    cv2.imshow("Hnad_Detection", img)
    if cv2.waitKey(1) & 0xFF == 27:
            break
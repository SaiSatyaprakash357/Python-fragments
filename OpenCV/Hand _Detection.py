from cvzone.HandTrackingModule import HandDetector
import cv2

cap = cv2.VideoCapture(0)

detector = HandDetector(staticMode=False, maxHands=1, modelComplexity=1, detectionCon=0.5, minTrackCon=0.5)
prev_fingers = []

while True:
    success, img = cap.read()
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
        
    cv2.imshow("Hnad_Detection", img)
    if cv2.waitKey(1) & 0xFF == 27:
            break
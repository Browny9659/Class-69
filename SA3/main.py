import cv2
from cvzone.HandTrackingModule import HandDetector


cap = cv2.VideoCapture(0)
cap.set(3, 1280)
cap.set(4, 720)

detector = HandDetector(detectionCon=0.8)


while True:

    try:
        check, cameraFeedImg = cap.read()
        cameraFeedImg = cv2.flip(cameraFeedImg, 1)

        handsDetector = detector.findHands(cameraFeedImg, flipType=False)
        hands = handsDetector[0]
        cameraFeedImg = handsDetector[1]

        if hands:
            hand1 = hands[0]
            lmList1 = hand1["lmList"]
            handType1 = hand1["type"]

            # Identify the fingers
            fingers1 = detector.fingersUp(hand1)

            currentFingerUp = ""

            # Write a condition for each finger identity and store the finger type into currentFingerUp variable
            if fingers1[0] == 1:
                currentFingerUp = "Thumb"
            elif fingers1[1] == 1:
                currentFingerUp = "Index Finger"
            elif fingers1[2] == 1:
                currentFingerUp = "Middle Finger"
            elif fingers1[3] == 1:
                currentFingerUp = "Ring Finger"
            elif fingers1[4] == 1:
                currentFingerUp = "Little Finger"
            else:
                currentFingerUp = ""

            # Show the currentFingerUp value on the camera feed
            cv2.putText(cameraFeedImg, handType1 + " : " + currentFingerUp, (75, 90),
                        cv2.FONT_HERSHEY_SIMPLEX, 0.7, (0, 0, 255), 2)

    except Exception as e:
        print(e)

    cv2.imshow("Image", cameraFeedImg)
    cv2.waitKey(1)
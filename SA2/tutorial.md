Detect Hands
=======================


In this activity, you will learn to detect the hands shown in the video feed using:



<img src= "https://media.slid.es/uploads/1525749/images/10509600/SA2-new2.gif" width = "480" height = "320">




Follow the given steps to complete this activity:
1. Import the HandTrackingModule


* Open file main.py.


* Import `HandDetector` from `cvzone.HandTrackingModule`.


    `from cvzone.HandTrackingModule import HandDetector`


* Creating an object to detect the hand.


* Set the `detectionCon` threshold to `0.8`.


    `detector = HandDetector(detectionCon=0.8)`




2. Detect a hand in cameraFeedImg


* Use the `detector.findHands()` method and pass `cameraFeedImg` set `flipType` to `False` as parameters.


    `handsDetector = detector.findHands(cameraFeedImg, flipType=False)`


* Get the first and second detected frames and store them in variable `hands` and `cameraFeedImg`.


    `hands = handsDetector[0]`


    `cameraFeedImg = handsDetector[1]`


3. Detect the hand


* Check if the first frame is detected using the `if` condition.


    `if hands:`


* Set `hands[0]` to `hand1` variable.
 
    `hand1 = hands[0]`


* Store the list of 21 Landmark points in `lmList1` variable.


    `lmList1 = hand1["lmList"]`


* Get the handType and store it in `handType1` variable.


    `handType1 = hand1["type"]  # Handtype Left or Right


* Save and run the code to check the output.

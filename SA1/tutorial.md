Open Camera
============


In this activity, you will learn to open the camera on your device using .




<img src= "https://media.slid.es/uploads/1525749/images/10509559/SA1.png" width = "480" height = "320">




Follow the given steps to complete this activity:
1. Open camera and capture the video


* Open file main.py.


* Import cv2 library.


  `import cv2`


* Capture the camera feed using `cv2.VideoCapture(0)` and set the resolution of the width and height of the video using `cap.set()` function.


  `cap = cv2.VideoCapture(0)`


  `cap.set(3, 1280)`


  `cap.set(4, 720)`


2. Read the video


* Use the while loop to display the video.


  `while True:`


* Write a try-except block in the while loop.


 
    `try:`
   
    `except Exception as e:`
        `print(e)`


* Get the single capture from camera using `cap.read()` method and store in the variable `check, cameraFeedImg`.


  ` check, cameraFeedImg = cap.read()`


* Flip the camera by using `cv2.flip()` and pass the cameraFeedImg to it.
  `cameraFeedImg = cv2.flip(cameraFeedImg, 1)`


* Save and run the code to check the output.

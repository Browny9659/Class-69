Identify the Fingers
=======================

In this activity, you will learn to Identify the fingers in the video.


<img src= "https://media.slid.es/uploads/1525749/images/10509613/ezgif.com-optimize.gif" width = "480" height = "320">






Follow the given steps to complete this activity:
1. Detect the fingers


* Open file main.py.


* Create a variable currentFingerUp and set an empty string to it.


    `currentFingerUp = ""`
       
* Use the conditional statement to check the fingers and store their names.


            `if fingers1[0]== 1:`


                `currentFingerUp="Thumb"`


            `elif fingers1[1] == 1:`


                `currentFingerUp = "Index Finger"`


            `elif fingers1[2] == 1:`


                `currentFingerUp = "Middle Finger"`


            `elif fingers1[3] == 1:`


                `currentFingerUp = "Ring Finger"`


            `elif fingers1[4] == 1:`


                `currentFingerUp = "Little Finger"`


            `else:`


                `currentFingerUp = ""`


* Use putText() to write the name of the finger on the screen.
     
        `cv2.putText(cameraFeedImg, handType1 + " : " + currentFingerUp , (75, 90),`
                        cv2.FONT_HERSHEY_SIMPLEX, 0.7, (0, 0, 255), 2)`


* Show the final image using `imshow()`.


    `cv2.imshow("Image", cameraFeedImg)`
    `cv2.waitKey(1)`
   
* Save and run the code to check the output.


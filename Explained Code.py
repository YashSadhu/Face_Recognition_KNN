import numpy as np
import cv2

# Here, we import two essential libraries:
# numpy: This library provides support for large, multi-dimensional arrays and matrices,
#        along with a large collection of high-level mathematical functions to operate on these arrays.
# cv2: This is the OpenCV library for Python. It is used for image and video processing,
#      including capturing video streams, image manipulation, and implementing computer vision algorithms.

face_cascade = cv2.CascadeClassifier('haarcascade_frontalface_alt.xml')
eye_cascade = cv2.CascadeClassifier('haarcascade_eye.xml')

# In this section, we load pre-trained Haar Cascade classifiers for face and eye detection.
# These classifiers are XML files that contain the trained model parameters.
# The cv2.CascadeClassifier function is used to load these XML files.
# We load two classifiers:
# haarcascade_frontalface_alt.xml: This is a Haar Cascade classifier for detecting frontal faces in images or video streams.
# haarcascade_eye.xml: This classifier is used for detecting eyes within detected face regions.

cap = cv2.VideoCapture(0)
# This line creates a VideoCapture object to read from the default camera (0 represents the built-in webcam).

while True:
    ret, frame = cap.read()
    # This line reads a frame from the camera. ret is a boolean that indicates whether the frame was read successfully,
    # and frame is the actual frame data (a NumPy array representing the image).

    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    # This line converts the color frame to grayscale, as Haar Cascades work better on grayscale images.

    faces = face_cascade.detectMultiScale(gray, 1.3, 5)
    # This line detects faces in the grayscale frame using the loaded face cascade classifier.
    # The detectMultiScale function returns a list of rectangles (x, y, width, height) for each detected face.

    for (x, y, w, h) in faces:
        cv2.rectangle(frame, (x, y), (x + w, y + h), (255, 0, 0), 2)
        # This line draws a red rectangle around the detected face on the original color frame.

        roi_gray = gray[y:y + h, x:x + w]
        roi_color = frame[y:y + h, x:x + w]

        eyes = eye_cascade.detectMultiScale(roi_gray)
        # This line detects eyes within the grayscale ROI using the loaded eye cascade classifier.

        for (ex, ey, ew, eh) in eyes:
            cv2.rectangle(roi_color, (ex, ey), (ex + ew, ey + eh), (0, 255, 0), 2)
            # This line draws a green rectangle around each detected eye on the color ROI.

    cv2.imshow('img', frame)
    # This line displays the processed frame with the detected faces and eyes outlined.

    if cv2.waitKey(1) & 0xFF == ord('q'):
        break
        # This line checks if the user has pressed the 'q' key.
        # If 'q' is pressed, the loop breaks, and the program exits.

cap.release()
# This line releases the camera resources.

cv2.destroyAllWindows()
# This line closes all the windows opened by OpenCV.

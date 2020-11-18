import cv2
import numpy as np

cap = cv2.VideoCapture(0)

while True:

    _, panel = cap.read()

    cv2.imshow("panel", panel)

    k = cv2.waitKey(30)
    if k == 27:
        break


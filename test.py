import cv2
import numpy as np

cap = cv2.VideoCapture(0)

r = g = b = 0

while True:

    _, frame = cap.read()

    cv2.imshow("panel", frame)

    height, width, channels = frame.shape

    b = frame[width//2, height//2, 0]
    g = frame[width//2, height//2, 1]
    r = frame[width//2, height//2, 2]

    # print(r, g, b)

    k = cv2.waitKey(30)
    if k == 27:
        break

print(r, g, b)


cnt = 0

range = 100

def check(check_r, check_g, check_b):
    if(check_r >= r-range and check_r <= r+range and check_g >= g-range and check_g <= g+range and check_b >= b-range and check_b <= b+range ) :
        return True
    else:
        return False

last = False

while True:

    _, frame = cap.read()

    cv2.imshow("panel", frame)

    height, width, channels = frame.shape

    temp_b = frame[width//2, height//2, 0]
    temp_g = frame[width//2, height//2, 1]
    temp_r = frame[width//2, height//2, 2]

    # print(r, g, b)
    current = check(temp_r, temp_g, temp_b)
    
    if(current != last):
        cnt += 1

    last = current

    k = cv2.waitKey(30)
    if k == 27:
        break


print("The answer is", cnt)

print(cnt // 2)


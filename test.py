import cv2
import numpy as np

cap = cv2.VideoCapture(0)

# r = g = b = 0

# List = [['Geeks', 'For'] , ['Geeks']]

n = 15

store_colors = [[[0]*n]*n]*3

box_range = 20

start_x = 0
end_x = 0
start_y = 0
end_y = 0

while True:

    _, frame = cap.read()

    cv2.imshow("panel", frame)

    height, width, channels = frame.shape


    #fix this
    cv2.rectangle(frame, (start_x, start_y), (end_x, end_y), (255,0,0), 2)

    

    store_colors = frame[start_x:(end_x+1), start_y:(end_y+1), 0:3]


    # b = frame[width//2, height//2, 0]
    # g = frame[width//2, height//2, 1]
    # r = frame[width//2, height//2, 2]

    start_x = width//2 - box_range
    end_x = width//2 + box_range
    start_y = height//2 - box_range
    end_y = height//2 + box_range

    # print(r, g, b)

    k = cv2.waitKey(30)
    if k == 27:
        break

# print(r, g, b)

# print(store_colors)

print("Background registered")

while True:
    _, frame = cap.read()

    cv2.imshow("panel", frame)
    k = cv2.waitKey(30)
    if k == 27:
        break

print("Timer started")

cnt = 0

check_range = 30

def check(x, y):
    if(x >= y-check_range and x <= y+check_range ) :
        return True
    else:
        return False

last = False

frames_skipped = 0

while True:

    

    _, frame = cap.read()

    cv2.imshow("panel", frame)

    height, width, channels = frame.shape

    # temp_b = frame[width//2, height//2, 0]
    # temp_g = frame[width//2, height//2, 1]
    # temp_r = frame[width//2, height//2, 2]

    cv2.rectangle(frame, (start_x, start_y), (end_x, end_y), (255,0,0), 2)

    if frames_skipped < 5:
        frames_skipped += 1
        continue

    # print(r, g, b)

    temp_store_colors = frame[start_x:(end_x+1), start_y:(end_y+1), 0:3]

    current = True

    for i in range(0, 11):
        for j in range(0, 11):
            for k in range(0, 3):
                current = current and check(temp_store_colors[i][j][k], store_colors[i][j][k])

    # current = check(temp_b, temp_g, temp_r)
    print("Checking")
    if(current != last):
        cnt += 1
        print("Count increased")

    last = current

    frames_skipped = 0

    k = cv2.waitKey(30)
    if k == 27:
        break


print("The answer is", cnt//2)

print("Count is", cnt)


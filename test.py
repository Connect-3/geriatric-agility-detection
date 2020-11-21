import cv2
import numpy as np

cap = cv2.VideoCapture(0)

# r = g = b = 0

# List = [['Geeks', 'For'] , ['Geeks']]




box_range = 30

n = box_range*2+10

store_colors = [[[]*n]*n]*3

start_x = 0
end_x = 0
start_y = 0
end_y = 0

_, frame = cap.read()

height, width, channels = frame.shape


start_x = width//2 - box_range
end_x = width//2 + box_range
start_y = height//2 - box_range
# start_y = height//2 - box_range//2


end_y = height//2 + box_range

start_y -= 200
end_y -= 200

# start_y -= 


# cv2.rectangle(frame, (start_x, start_y), (end_x, end_y), (255,0,0), 2)





while True:

    _, frame = cap.read()

    # height, width, channels = frame.shape

    cv2.rectangle(frame, (start_x, start_y), (end_x, end_y), (255, 0, 0), 2)
    # cv2.rectangle(frame, (start_x-50, start_y-50), (end_x+50, end_y+50), (255,255,0), 2)
    


    cv2.imshow("panel", frame)

    

    store_colors = frame[ start_y:(end_y+1) , start_x:(end_x+1), 0:3]


    # b = frame[width//2, height//2, 0]
    # g = frame[width//2, height//2, 1]
    # r = frame[width//2, height//2, 2]

    



    # print(r, g, b)

    k = cv2.waitKey(30)
    if k == 27:
        break

# print(r, g, b)

# print(store_colors.shape)
# print(store_colors)

# print(frame.shape)

print("Background registered")

while True:
    _, frame = cap.read()


    cv2.rectangle(frame, (start_x, start_y), (end_x, end_y), (255,0,0), 2)
    # cv2.rectangle(frame, (start_x-50, start_y-50), (end_x+50, end_y+50), (255,255,0), 2)


    cv2.imshow("panel", frame)
    cv2.imshow("color taken", store_colors)
    k = cv2.waitKey(30)
    if k == 27:
        break



print("Timer started")

cnt = 0

check_range = 40

def check(x, y):
    if(x >= y-check_range and x <= y+check_range ) :
        return True
    else:
        return False

last = True

frames_skipped = 0

while True:

    

    _, frame = cap.read()

    cv2.rectangle(frame, (start_x, start_y), (end_x, end_y), (255,0,0), 2)
    # cv2.rectangle(frame, (start_x-50, start_y-50), (end_x+50, end_y+50), (255,255,0), 2)



    # cv2.circle(frame, (width//2, height//2), 2, (0, 0, 255), 2)


    cv2.imshow("panel", frame)

    height, width, channels = frame.shape

    # temp_b = frame[width//2, height//2, 0]
    # temp_g = frame[width//2, height//2, 1]
    # temp_r = frame[width//2, height//2, 2]

    cv2.rectangle(frame, (start_x, start_y), (end_x+1, end_y+1), (255,0,0), 2)

    # if frames_skipped < 1:
    #     frames_skipped += 1
    #     continue

    # print(r, g, b)

    temp_store_colors = frame[ start_y:(end_y+1) , start_x:(end_x+1), 0:3]

    # print(temp_store_colors.shape)

    current = True
    for i in range(0, box_range*2):
        for j in range(0, box_range*2):
            for k in range(0, 3):
                current = current and check(temp_store_colors[i][j][k], store_colors[i][j][k])


    cv2.imshow("Checking", temp_store_colors)
    # print("Current is ", current)
    # print("Last was ", last)
    # current = check(temp_b, temp_g, temp_r)

    # print("Start x is", start_x)
    # print("Start y is", start_y)
    # print("End x is", end_x)
    # print("End y is", end_y)
    print("Checking")
    if(current != last):
        cnt += 1
        print(frame[width//2, height//2])
        print("Count increased")

    last = current

    frames_skipped = 0

    k = cv2.waitKey(30)
    if k == 27:
        break


print("The answer is", cnt//2)

print("Count is", cnt)


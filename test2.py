import cv2
import numpy as np

# cap = cv2.VideoCapture(0)
cap = cv2.VideoCapture(0, cv2.CAP_DSHOW) #captureDevice = camera
box_range = 30
n = box_range*2+10
check_range = 40
# last = True
# cnt = 0

def check(x, y):
    if(x >= y-check_range and x <= y+check_range ) :
        return True
    else:
        return False

store_colors = [[[]*n]*n]*3

_, frame = cap.read()
# cap.release()
height, width, channels = frame.shape

start_x = width//2 - box_range
end_x = width//2 + box_range
start_y = height//2 - box_range
end_y = height//2 + box_range
start_y -= 200
end_y -= 200


# print(last)


def register_Background():
    
    
    while True:
        _, frame = cap.read()
        cv2.rectangle(frame, (start_x, start_y), (end_x, end_y), (255, 0, 0), 2)
        cv2.imshow("panel", frame)
        store_colors = frame[ start_y:(end_y+1) , start_x:(end_x+1), 0:3]
        k = cv2.waitKey(30)
        if k == 27:
            print("Background registered")
            cv2.destroyAllWindows()
            break


    while True:
        _, frame = cap.read()
        cv2.rectangle(frame, (start_x, start_y), (end_x, end_y), (255,0,0), 2)
        cv2.imshow("panel", frame)
        cv2.imshow("color taken", store_colors)
        k = cv2.waitKey(30)
        if k == 27:
            break
    t1 = threading.Thread(target=Timer)
    t1 = thread_with_trace(target=Timer)
    t2 = thread_with_trace(target=loop3(store_colors))
    # t2 = threading.Thread(target=loop3)
    t1.start()
    t2.start()
    if not t1.is_alive(): 
        t2.kill()
    # loop3(store_colors)
    

def loop3(store_colors):
    print("Timer started")
    print(store_colors)
    last = True
    cnt=0
    while True:
        _, frame = cap.read()
        cv2.rectangle(frame, (start_x, start_y), (end_x, end_y), (255,0,0), 2)
        cv2.imshow("panel", frame)
        height, width, channels = frame.shape
        cv2.rectangle(frame, (start_x, start_y), (end_x+1, end_y+1), (255,0,0), 2)
        temp_store_colors = frame[ start_y:(end_y+1) , start_x:(end_x+1), 0:3]
        current = True
        for i in range(0, box_range*2):
            for j in range(0, box_range*2):
                for k in range(0, 3):
                    current = current and check(temp_store_colors[i][j][k], store_colors[i][j][k])

        cv2.imshow("Checking", temp_store_colors)
        print("Checking")
        if(current != last):
            cnt += 1
            print(frame[width//2, height//2])
            print("Count increased")
        last = current
        k = cv2.waitKey(30)
        if k == 27:
            break
    print("The answer is", cnt//2)
    print("Count is", cnt)
    cv2.destroyAllWindows()
# register_Background()
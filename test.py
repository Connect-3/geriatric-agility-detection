import cv2
import numpy as np
import time
import threading 
import sys
import os
import trace
# from gui import *

# cap = cv2.VideoCapture(0)
cap = cv2.VideoCapture(0, cv2.CAP_DSHOW) #captureDevice = camera
box_range = 25
n = box_range*2+10
check_range = 40
# last = True
cnt=0

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

t1=t2=0

# print(last)


def register_Background():
    
    
    while True:
        _, frame = cap.read()
        cv2.rectangle(frame, (start_x, start_y), (end_x, end_y), (157, 179, 69), 2)
        
        cv2.imshow("panel", frame)
       
        # font = cv2.Ar
        store_colors = frame[ start_y:(end_y+1) , start_x:(end_x+1), 0:3]
        # cv2.putText('Nikhil',(50,50)) 
        k = cv2.waitKey(30)
        if k == 27:
            print("Background registered")
            cv2.destroyAllWindows()
            break
            
    while True:
        _, frame = cap.read()
        cv2.rectangle(frame, (start_x, start_y), (end_x, end_y), (157,179,69), 2)
        cv2.imshow("panel", frame)
        cv2.imshow("color taken", store_colors)
        k = cv2.waitKey(30)
        if k == 27:
            break
    cv2.destroyAllWindows()
    print("Timer started")
    global t1
    global t2
    # t1 = thread_with_trace(target=Timer)
    # t2 = thread_with_trace(target=loop3,args=(store_colors, ))
    t1 = threading.Thread(target=Timer)
    t2 = threading.Thread(target=loop3,args=(store_colors, ))
    t1.start()
    t2.start()
    t1.join()
    t2.join()
    print("Cnt in end of register background is {}".format(cnt))
    return cnt
    
    
# def Timer():
#     i=-1;
#     l_time=True
#     last_time=time.time()
#     font = cv2.FONT_HERSHEY_SIMPLEX 
#     org = (50, 50) 
#     fontScale = 1 
#     color = (101, 138, 255) 
#     thickness = 2
#     image=cv2.imread("download.png")
#     cv2.imshow("panel",image)
    

#     while(True):
#         image = cap.read()
#         # cv2.rectangle(frame, (start_x, start_y), (end_x, end_y), (157, 179, 69), 2)
#         # cv2.imshow("panel", img)
#         # curr_time = time.time()
#         # # print("Seconds since epoch =", curr_time)	
#         # if(curr_time-last_time>=1):
#         #     l_time=True
#         # if(l_time==True):
#         #     i=i+1
#         #     last_time=curr_time
#         #     l_time=False
#         i=i+1
#         image=cv2.putText(image,str(i), org, font,  
#             fontScale, color, thickness, cv2.LINE_AA) 
#         cv2.imshow("panel", image)
#         k = cv2.waitKey(0) & 0xFF
def loop3(store_colors):
    last = True
    global cnt
    while (t1.is_alive()):
        _, frame = cap.read()
        cv2.rectangle(frame, (start_x, start_y), (end_x, end_y), (157, 179, 69), 2)
        
        cv2.imshow("panel", frame)
        height, width, channels = frame.shape
        cv2.rectangle(frame, (start_x, start_y), (end_x+1, end_y+1), (157, 179, 69), 2)
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
    # loop3(store_colors)
    print("The answer is", cnt//2)
    print("Count is", cnt)
    cv2.destroyAllWindows()
#         if k == 27:  
#             cv2.destroyAllWindows() 
      


def Timer():
   
    # Check if camera opened successfully 
    cap = cv2.VideoCapture('timer.mp4')
       
    if (cap.isOpened()== False):  
        print("Error opening video  file") 

    while(cap.isOpened()): 
        
    # Capture frame-by-frame 
        ret, frame = cap.read() 
        if ret == True: 
        
            # Display the resulting frame 
            cv2.imshow('Frame', frame) 
            # fps = frame.get(cv2.cv.CV_CAP_PROP_FPS)
            # print(fps)
            # Press Q on keyboard to  exit 
            if cv2.waitKey(25) & 0xFF == ord('q'): 
                break 
        else:  
              break
              
    # When everything done, release  
    # the video capture object 
    cap.release() 
    
    # Closes all the frames 
    cv2.destroyAllWindows() 
 

     
        # def final():
#     t1 = threading.Thread(target=loop3)
#     t2 = threading.Thread(target=Timer) 
  
#     # starting thread 1 
#     t1.start() 
#     # starting thread 2 
#     t2.start() 
  
#     # wait until thread 1 is completely executed 
#     t1.join() 
#     # wait until thread 2 is completely executed 
#     t2.join() 
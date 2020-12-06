#imports
import cv2
import threading 

#capture webcam
cap = cv2.VideoCapture(0) 

#play variables
box_range = 25 #from the centre so each side of box is 2 * box_range
check_range = 40 #we can decide till what value does the program consider a colour as same

#total number of times the background changes so answer is really cnt//2
cnt=0
n = box_range*2+10

#function to actually check if 2 colours should be considered same
def check(x, y):
    if(x >= y-check_range and x <= y+check_range ) :
        return True
    else:
        return False

#matrix for registration of background color 
store_colors = [[[]*n]*n]*3
_, frame = cap.read()
height, width, channels = frame.shape

#setting actual coordinates of the box for checking colour
start_x = width//2 - box_range
end_x = width//2 + box_range
start_y = height//2 - box_range
end_y = height//2 + box_range
start_y -= 200
end_y -= 200

#making threads global
t1=t2=0

#function to return count of complete chair stands
def register_Background():
    #first loop to register background by storing  in a variable called 'store_colors'
    #a loop is used to play a video in the form of multiple frames(images)
    while True:
        #taking a frame from the video
        _, frame = cap.read()
        #drawin the box
        cv2.rectangle(frame, (start_x, start_y), (end_x, end_y), (157, 179, 69), 2)
        #showing the panel to the user
        cv2.imshow("panel", frame)
       
        #storing colors for checking later
        store_colors = frame[ start_y:(end_y+1) , start_x:(end_x+1), 0:3]
       
        #if enter is pressed then exit from the loop
        k = cv2.waitKey(30)
        if k == 13:
            print("Background registered")
            cv2.destroyAllWindows()
            break
    
    #2nd loop to give time to the user to properly adjust
    while True:
        _, frame = cap.read()
        cv2.rectangle(frame, (start_x, start_y), (end_x, end_y), (157,179,69), 2)
        cv2.imshow("panel", frame)
        cv2.imshow("color taken", store_colors)
        k = cv2.waitKey(30)
        if k == 13:
            break
    cv2.destroyAllWindows()
    print("Timer started")

    #making t1/t2 global so we can change them here and they'll actually change the global variables
    global t1
    global t2

    #making threads
    t1 = threading.Thread(target=Timer)
    t2 = threading.Thread(target=loop3,args=(store_colors, ))

    #starting threads
    t1.start()
    t2.start()

    #waiting for threads to finish before  continuing
    t1.join()
    t2.join()

    return cnt
    
def loop3(store_colors):
    #3rd loop which would actually look for change in the box by comparing with the already stored background
    last = True
    global cnt
    while (t1.is_alive()):
        _, frame = cap.read()
        cv2.rectangle(frame, (start_x, start_y), (end_x, end_y), (157, 179, 69), 2)
        cv2.imshow("panel", frame)
        height, width, channels = frame.shape
        cv2.rectangle(frame, (start_x, start_y), (end_x+1, end_y+1), (157, 179, 69), 2)

        #storing current colors in temp_store_colors
        temp_store_colors = frame[ start_y:(end_y+1) , start_x:(end_x+1), 0:3]

        current = True
        #if even 1 pixel does not match with the corresponding pixel in the background
        #we registered earlier then current will be False
        for i in range(0, box_range*2):
            for j in range(0, box_range*2):
                for k in range(0, 3):
                    current = current and check(temp_store_colors[i][j][k], store_colors[i][j][k])
        
        #displaying the portion of screen that is being checked against the original background
        cv2.imshow("Checking", temp_store_colors)
        print("Checking")

        #current = true implies that it is indeed equal to the background we registered earlier
        #so every time current and last are unequal that means there must have been a change in the background
        #hence we need to increase count
        if(current != last):
            cnt += 1
            print("Count increased")
        last = current
        k = cv2.waitKey(30)
        #exit on pressing escape key
        if k == 27:
            break
    print("The answer is ", cnt//2)
    print("Count is ", cnt)
    cv2.destroyAllWindows()

def Timer():
    cap = cv2.VideoCapture('Timer.mp4')
    if (cap.isOpened()== False):  
        print("Error opening video  file") 
    while(cap.isOpened()):    
    # Capture frame-by-frame 
        ret, frame = cap.read() 
        if ret == True: 
            # Display the resulting frame 
            cv2.imshow('Frame', frame) 
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
 


# Import required packages
import cv2
import numpy as np

# variable for counting saved images
count = 551

# Function for handling mouse event callback
def mouse_event(event,x,y,flags,params):
    global count
    if event == cv2.EVENT_LBUTTONDOWN:
        # Save clicked image
        cv2.imwrite('img{}.jpg'.format(count),frame)
        print('img{} downloaded sucesssfully..'.format(count))
        count = count+1

# Load video
cap = cv2.VideoCapture('insulator_19.mp4')

#Loop for Capture frame by frame
while(cap.isOpened()):
    ret , frame = cap.read()
    if ret:
        cv2.imshow("img",frame)
        # Set mouse event callback for continously monitor mouse events
        cv2.setMouseCallback('img',mouse_event)
        if cv2.waitKey(100) & 0xFF == ord('q'):
            break

    else:
        break
cap.release()
cv2.destroyAllWindows()





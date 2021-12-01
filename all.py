import cv2
import time
import numpy as np

# to save ioutput in a file output.avi
fourcc=cv2.VideoWriter_fourcc(*"XVID")
output=cv2.VideoWriter("output.avi",fourcc,20.0,(640,480))
#strating webcam
cap=cv2.VideoCapture(0)
#allowuing webcam to start  by makinf code sleep for 2 sec
time.sleep(2)
bg=0
#capturing backgorounf for 60 

for i in range(60):
    rep,bg=cap.read()
# falipping camera
bg=np.flip(bg,axis=1)
# reading the captured frame until camera is opened
while (cap.isOpened()):
    rep,ing=cap.read()
    if not rep:
        break
    ing=np.flip(ing,axis=1)
    # hue saruration value
    hsv=cv2.cvtColor(ing,cv2.COLOR_BGR2HSV())
    #generating mask to detec rd
    #theese values can also be changer per color
    lowerred=np.array([0,120,50])
    upperred=np.array([10,255,255])
    mask1=cv2.inRange(hsv,lowerred,upperred)
    lowerred=np.array([170,120,70])
    upperred=np.array([180,255,255])
    mask2=cv2.inRange(hsv,lowerred,upperred)
    mask1=mask1+mask2
#open and expand mask1 
    mask1=cv2.morphologyEx(mask1,cv2.MORPH_OPEN,np.ones((3,3),np.uint8))
    mask1=cv2.morphologyEx(mask1,cv2.MORPH_DILATE,np.ones((3,3),np.uint8))
    mask2=cv2.bitwise_not(mask1)
    res1=cv2.bitwise_and(ing,ing,mask=mask2)
    res2=cv2.bitwise_and(bg,bg,mask=mask1)
    finalout=cv2.addWeighted(res1,1,res2,1,0)
    output_file.write(finalout)
    cv2.imshow("magic",finalout)
    cv2.waitKey(1)
cap.release()
out.release()
cv2.destroyAllWindows()

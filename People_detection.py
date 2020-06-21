import cv2
import numpy as np
from datetime import*

file='record.txt'


face_classifier=cv2.CascadeClassifier("D:/Intern/haar-cascade-files-master/haarcascade_fullbody.xml")
cap=cv2.VideoCapture("vtest.avi")

d=[]
while cap.isOpened():
    dt=datetime.now()
    s=dt.second
    print(s)
    _,img=cap.read()
    img=cv2.resize(img,None,fx=0.8,fy=0.8,interpolation=cv2.INTER_LINEAR)
    gray= cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
    body=face_classifier.detectMultiScale(img,1.1,6) # x,y,w,h values
    
    
    date=str(datetime.now())
    for (x,y,w,h) in body:
        cv2.rectangle(img,(x,y),(x+w,y+h) ,(125,0,255),4)
        roi_gray=gray[y:y+h,x:x+w]
        roi_color=img[y:y+h,x:x+w]
        cv2.putText(img,date,(10,50),cv2.FONT_HERSHEY_COMPLEX,1,(0,255,0),2)
        f=len(body)
        print('count')
        print(f)
        
        with open(file,'a+') as files:
            files.write(str(dt)+'-'+str(f)+'\n')
            print('record saved')
            files.close()
        
    #c=len(faces)
    d.append(f)
    cv2.putText(img,str(f)+' Number of people',(400,450),cv2.FONT_HERSHEY_COMPLEX,1,(0,255,0),2)
    cv2.imshow("image",img)
    if cv2.waitKey(1)==27:
        break
print(c)
c=len(d)
print(max(d))
cap.release()
cv2.destroyAllWindows()

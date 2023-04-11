from ultralytics import YOLO
import cv2
import cvzone
import math


cap=cv2.VideoCapture(0)      #For Webcam
cap.set(3,640)
cap.set(4,480)


model=YOLO('HandSign.pt')

classNames = ['Power','Rock','Thumb Down','Thumb Up','Victory','Hi-Five']
while True:
    sucess,img=cap.read()
    mask=cv2.imread('Mask1.png')
    #imgreg=cv2.bitwise_and(img,mask)
    results=model(img,stream=True)
    HiFive=cv2.imread('hifive.png',cv2.IMREAD_UNCHANGED)
    power=cv2.imread('power.png',cv2.IMREAD_UNCHANGED)
    rock=cv2.imread('rock.png',cv2.IMREAD_UNCHANGED)
    thumbdown=cv2.imread('thumbdown.png',cv2.IMREAD_UNCHANGED)
    thumbup=cv2.imread('thumbup.png',cv2.IMREAD_UNCHANGED)
    victory=cv2.imread('victory.png',cv2.IMREAD_UNCHANGED)
    #img=cvzone.overlayPNG(img,Maskgraphics,(0,0))
    for r in results:
        boxes=r.boxes
        #Bounding Boxes
        for box in boxes:
            x1,y1,x2,y2=box.xyxy[0]
            x1,y1,x2,y2=int(x1),int(y1),int(x2),int(y2)
            print(x1,y1,x2,y2)
            cv2.rectangle(img,(x1,y1),(x2,y2),(255,0,0),3)

            #Confidence level
            conf=math.ceil((box.conf[0]*100))/100
            print(conf)

            #Add the values
            cls=int(box.cls[0])
            cvzone.putTextRect(img,f'{classNames[cls]} {conf}',(max(0,x1),max(35,y1)),scale=1,thickness=1)
#classNames = ['Power','Rock','Thumb Down','Thumb Up','Victory','Hi-Five']
            if classNames[cls]=='Thumb Up':
                img = cvzone.overlayPNG(img, thumbup, (0, 0))
            elif classNames[cls]=='Thumb Down':
                img=cvzone.overlayPNG(img,thumbdown,(0,0))
            elif classNames[cls]=='Hi-Five':
                img=cvzone.overlayPNG(img,HiFive,(0,0))
            elif classNames[cls]=='Rock':
                img=cvzone.overlayPNG(img,rock,(0,0))
            elif classNames[cls]=='Power':
                img=cvzone.overlayPNG(img,power,(0,0))
            elif classNames[cls]=='Victory':
                img=cvzone.overlayPNG(img,victory,(0,0))


    cv2.imshow("Image",img)
    cv2.waitKey(1)
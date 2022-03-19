import cv2
import mediapipe as mp
import time
import face_recognition
img=face_recognition.load_image_file("images\Ahmed Taha.jpg")
enc=face_recognition.face_encodings(img)[0]
#print(enc)
cap=cv2.VideoCapture(0)
ptime=0
mpFaceDetection=mp.solutions.face_detection
mpDraw=mp.solutions.drawing_utils
facedetection=mpFaceDetection.FaceDetection()
while True:
    _,img=cap.read()
    imgrgb=cv2.cvtColor(img,cv2.COLOR_BGR2RGB)
    results=facedetection.process(imgrgb)
    if results.detections:
        for detection in results.detections:
            ##mpDraw.draw_detection(img,detection)
            print(detection.score[0])
            bbox=detection.location_data.relative_bounding_box
            h,w,c=img.shape
            pos=int(bbox.xmin*w),int(bbox.ymin*h),int(bbox.width*w),int(bbox.height*h)
            cv2.rectangle(img,pos,(255,0,255),2)
            cv2.putText(img, f"{int(detection.score[0]*100)}%", (pos[0], pos[1]-20), cv2.FONT_HERSHEY_PLAIN, 2, (255, 0, 0), 2)


    ctime=time.time()
    fps=1/(ctime-ptime)
    ptime=ctime
    cv2.putText(img,f"Fps is:{int(fps)}",(10,30),cv2.FONT_HERSHEY_COMPLEX,1,(255,0,0),2)
    cv2.imshow("Image", img)
    if cv2.waitKey(1)==ord("q"):
        break



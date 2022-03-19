import os
import pickle
import face_recognition
import cv2
Names=[]
Encode=[]
with open('Train.pkl','rb') as f:
    Names=pickle.load(f)
    Encode=pickle.load(f)

cap=cv2.VideoCapture(0)
while cap.isOpened():
    _,frame=cap.read()
    framergb=cv2.cvtColor(frame,cv2.COLOR_BGR2RGB)
    facepos=face_recognition.face_locations(framergb)
    allencode=face_recognition.face_encodings(framergb,facepos)
    for (ymin,xmax,ymax,xmin),encode in zip(facepos,allencode):
        matches=face_recognition.compare_faces(encode,Encode)
        name='Unkown'
        if True in matches:
            name=Names[matches.index(True)]
        cv2.rectangle(frame,(xmin,ymin),(xmax,ymax),(255,255,255),2)
        cv2.putText(frame,name,(xmin-5,ymin-5),cv2.FONT_HERSHEY_SIMPLEX,0.8,(0,0,0),1)
    cv2.imshow('Window',frame)
    if cv2.waitKey(1)==ord('q'):
        break
import cv2
import face_recognition
import pickle
Encode=[]
Names=[]
with open('Train.pkl','rb') as f:
    Names=pickle.load(f)
    Encode=pickle.load(f)
cam=cv2.VideoCapture(0)
#cam.set(3,1280)
#cam.set(4,720)
#print(Names)
#print(Encode)
while True:
    _,frame=cam.read()
    smallframe=cv2.resize(frame,(0,0),fx=0.33,fy=0.33)
    frameRGB=cv2.cvtColor(smallframe,cv2.COLOR_BGR2RGB)
    facePositions=face_recognition.face_locations(frameRGB)
    allencodeings=face_recognition.face_encodings(frameRGB,facePositions)
    for (top,right,bottom,left),face_enc in zip(facePositions,allencodeings):
        name='Unkown Person'
        matches=face_recognition.compare_faces(Encode,face_enc)
        if True in matches:
            match_index=matches.index(True)
            name=Names[match_index]
        top=top*3
        right=right*3
        bottom=bottom*3
        left=left*3
        cv2.rectangle(frame,(left,top),(right,bottom),(0,0,255),2)
        cv2.putText(frame,name,(left,top-5),cv2.FONT_HERSHEY_SIMPLEX,0.75,(0,0,255),2)
    cv2.imshow("Frame",frame)
    if cv2.waitKey(1)==ord('q'):
        break
cam.release()
cv2.destroyAllWindows()


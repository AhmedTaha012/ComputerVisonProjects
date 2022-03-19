import cv2
import mediapipe as mp
import time
cap=cv2.VideoCapture(0)
cap.set(3,1280)
cap.set(4,1080)
mpHands=mp.solutions.hands
hand=mpHands.Hands()
mpdraw=mp.solutions.drawing_utils
ptime=0
while cap.isOpened():
    success,frame=cap.read()
    frame=cv2.flip(frame,1)
    imgRgb=cv2.cvtColor(frame,cv2.COLOR_BGR2RGB)
    results=hand.process(imgRgb)
    if results.multi_hand_landmarks:
        for handlms in results.multi_hand_landmarks:
            for id,lm in enumerate(handlms.landmark):
                h,w,c=frame.shape
                print(id,lm.x,lm.y)
                cx,cy=int(lm.x*w),int(lm.y*h)
                cv2.circle(frame,(cx,cy),25,(255,0,255),cv2.FILLED)

            mpdraw.draw_landmarks(frame,handlms,mpHands.HAND_CONNECTIONS)

    ctime = time.time()
    fps = 1 / (ctime - ptime)
    ptime = ctime
    cv2.putText(frame, f"Fps is:{int(fps)}", (10, 30), cv2.FONT_HERSHEY_COMPLEX, 1, (255, 0, 0), 2)


    cv2.imshow("frame",frame)
    if cv2.waitKey(1)==ord('q'):
        break
cv2.destroyAllWindows()
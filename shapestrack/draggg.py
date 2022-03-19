import cv2
import mediapipe as mp
cap=cv2.VideoCapture(0)
mpHands=mp.solutions.hands
hand=mpHands.Hands()
cap.set(3,1280)
cap.set(4,1080)
while True:
    rect,frame=cap.read()
    frame = cv2.flip(frame, 1)
    imgRgb = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
    results = hand.process(imgRgb)
    pos1 = (0, 0)
    pos2 = (200, 200)
    cv2.rectangle(frame, pos1, pos2, (255, 0, 255), -1)
    if results.multi_hand_landmarks:
        for hand_landmarks in results.multi_hand_landmarks:
            x,y=hand_landmarks.landmark[4].x,hand_landmarks.landmark[4].y
            x=int(x*frame.shape[1])
            y =int(y * frame.shape[0])
            print(x,y)
            #cv2.circle(frame,(x,y),20,(0,0,255),-1)

            if x ==(pos2[0]-pos1[1])/2 and y ==(pos2[0]-pos1[1])/2:
                pos1=(60,60)
                pos2=(130,130)

    cv2.imshow('Frame', frame)
    if cv2.waitKey(1)==ord('q'):
        break

cap.release()
cv2.destroyAllWindows()
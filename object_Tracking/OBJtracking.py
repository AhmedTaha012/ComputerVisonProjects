import cv2
cap=cv2.VideoCapture(0)
cap.set(3,1920)
cap.set(4,1080)
traker=cv2.TrackerMOSSE_create()
#traker=cv2.TrackerCSRT_create()
def program():
    while cap.isOpened():
        timer = cv2.getTickCount()
        _, frame = cap.read()
        cv2.flip(frame, 1)
        succ, bbox = traker.update(frame)
        print(frame.shape)
        print(succ, bbox)
        if succ and (0 < bbox[0] < 480) and (0 < bbox[0] < 640):
            drawbox(frame, bbox)
        else:
            cv2.putText(frame, "Lost", (75, 75), cv2.FONT_HERSHEY_SIMPLEX, 0.7, (0, 0, 255), 2)

        fps = cv2.getTickFrequency() / (cv2.getTickCount() - timer)
        cv2.putText(frame, str(int(fps)), (75, 50), cv2.FONT_HERSHEY_SIMPLEX, 0.7, (0, 0, 255), 2)
        cv2.imshow("Frame", frame)

        if cv2.waitKey(1) & 0xff == ord('q'):
            break

def drawbox(img,bbox):
    x,y,w,h=int(bbox[0]),int(bbox[1]),int(bbox[2]),int(bbox[3])
    cv2.rectangle(img,(x,y),((x+w),(y+h)),(255,0,255),2,1)
    cv2.putText(frame, "tracking", (75, 75), cv2.FONT_HERSHEY_SIMPLEX, 0.7, (255, 0, 0), 2)
while True:
    print(f"Enter s to can start capture")
    img=cv2.imread("images.png")
    if cv2.waitKey(1) & 0xff==ord('s'):
        succ1, frame = cap.read()
        bbox = cv2.selectROI("Traking", frame, False)
        traker.init(frame, bbox)
        program()
    cv2.imshow("File", img)





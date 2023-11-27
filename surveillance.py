import time
from ultralytics import YOLO
import cv2 as cv
model = YOLO('yolov8n.pt')


cap = cv.VideoCapture(0)


cTime = 0
pTime = 0
while True:
    success, img = cap.read()
    #img = cv.flip(img, 1)
    results = model(img)
    for detection in results[0]:
        x = detection.boxes.cls
        if int(x) == 0:
            detection = detection.boxes.xyxy
            x1, y1, x2, y2 = detection[0]
            cv.rectangle(img, (int(x1), int(y1)), (int(x2), int(y2)), (0, 255, 0), 2)
            cv.putText(img, "Person", (int(x1), int(y1)), cv.FONT_HERSHEY_PLAIN, 2,
                       (0, 255, 0), 2)
    cTime = time.time()
    fps = 1 / (cTime - pTime)
    pTime = cTime

    cv.putText(img, str(int(fps)), (10, 70), cv.FONT_HERSHEY_PLAIN, 3,
               (255, 0, 255), 3)


    cv.imshow('img', img)
    if cv.waitKey(1) & 0xFF == ord('q'):
        break

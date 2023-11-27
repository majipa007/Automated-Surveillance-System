
import cv2 as cv
import time
from ultralytics import YOLO


def load_model():
    model = YOLO('yolov8n.pt')
    return model


class Object_Detection:
    def __init__(self, capture_index):
        self.model = load_model()

    def predict(self, frame):
        results = self.model(frame)
        return results

    def __call__(self, *args, **kwargs):
        self.cTime = 0
        self.pTime = 0
        cap = cv.VideoCapture(0)
        assert cap.isOpened()
        cap.set(cv.CAP_PROP_FRAME_WIDTH, 640)
        cap.set(cv.CAP_PROP_FRAME_HEIGHT, 480)

        while True:
            self.cTime = time.time()
            success, img = cap.read()
            img = cv.flip(img, 1)
            results = self.predict(img)
            for detection in results[0]:
                x = detection.boxes.cls
                if int(x) == 0:
                    detection = detection.boxes.xyxy
                    x1, y1, x2, y2 = detection[0]
                    cv.rectangle(img, (int(x1), int(y1)), (int(x2), int(y2)), (0, 255, 0), 2)
                    cv.putText(img, "Person", (int(x1), int(y1)), cv.FONT_HERSHEY_PLAIN, 2,
                               (0, 255, 0), 2)
            fps = 1 / (self.cTime - self.pTime)
            self.pTime = self.cTime

            cv.putText(img, str(int(fps)), (10, 70), cv.FONT_HERSHEY_PLAIN, 3,
                       (255, 0, 255), 3)

            cv.imshow('img', img)
            if cv.waitKey(1) & 0xFF == ord('q'):
                break

        cap.release()
        cv.destroyAllWindows()


# detector = Object_Detection(capture_index=0)
# detector()

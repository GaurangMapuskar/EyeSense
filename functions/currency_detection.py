import cv2
from turtle import home
from ultralytics import YOLO
from flask import redirect, url_for

def generate_frames():
    cap = cv2.VideoCapture(0)
    cap.set(3, 640)
    cap.set(4, 480)
    font = cv2.FONT_HERSHEY_COMPLEX

    model = YOLO('functions/Currency.pt')

    while True:
        success, imgOrignal = cap.read()

        # Run object detection on the input frame
        results = model(imgOrignal, conf=0.25)

        for detection in results[0].boxes:
            print(detection.xyxy)
            x1 = int(detection.xyxy[0][0])
            y1 = int(detection.xyxy[0][1])
            x2 = int(detection.xyxy[0][2])
            y2 = int(detection.xyxy[0][3])

            class_id = detection.cls[0]
            conf = detection.conf[0]

            # Draw bounding box and label
            cv2.rectangle(imgOrignal, (x1, y1), (x2, y2), (0, 255, 0), 2)
            cv2.putText(imgOrignal, f'{model.names[int(class_id)]} {conf:.2f}', (x1, y1 - 10), font, 0.75,
                        (255, 255, 255), 1, cv2.LINE_AA)

        ret, frame = cv2.imencode('.jpg', imgOrignal)
        yield (b'--frame\r\n' b'Content-Type: image/jpeg\r\n\r\n' + bytearray(frame) + b'\r\n')

        k = cv2.waitKey(1)
        if k == ord('q'):
            cap.release()
            cv2.destroyAllWindows()
            return redirect(url_for('index'))

def currency_detection():
    return generate_frames()

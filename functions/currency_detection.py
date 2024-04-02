import cv2
from turtle import home
from ultralytics import YOLO
from camera import VideoCamera
from flask import redirect, url_for

def currency_detection():
    video_camera = VideoCamera()

    model = YOLO('functions/Currency.pt')

    while True:
        frame = video_camera.get_frame()
        font = cv2.FONT_HERSHEY_COMPLEX
        # Run object detection on the input frame
        results = model(frame, conf=0.25)

        for detection in results[0].boxes:
            print(detection.xyxy)
            x1 = int(detection.xyxy[0][0])
            y1 = int(detection.xyxy[0][1])
            x2 = int(detection.xyxy[0][2])
            y2 = int(detection.xyxy[0][3])

            class_id = detection.cls[0]
            conf = detection.conf[0]

            # Draw bounding box and label
            cv2.rectangle(frame, (x1, y1), (x2, y2), (0, 255, 0), 2)
            cv2.putText(frame, f'{model.names[int(class_id)]} {conf:.2f}', (x1, y1 - 10), font, 0.75,
                        (255, 255, 255), 1, cv2.LINE_AA)
            
            ret, encoded_frame = cv2.imencode('.jpg', frame)
            yield (b'--frame\r\n' b'Content-Type: image/jpeg\r\n\r\n' + bytearray(encoded_frame) + b'\r\n')

        k = cv2.waitKey(1)
        if k == ord('q'):
            cap.release()
            cv2.destroyAllWindows()


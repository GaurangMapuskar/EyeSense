import cv2
from turtle import home
from ultralytics import YOLO
import numpy as np
from flask import redirect, url_for
from camera import VideoCamera

def object_detection():
    # Create an instance of VideoCamera
    video_camera = VideoCamera()

    # Load the YOLO object detection model
    model = YOLO('functions/best.pt')

    font = cv2.FONT_HERSHEY_COMPLEX

    while True:
        # Get frame from VideoCamera
        frame = video_camera.get_frame()

        # Run object detection on the input frame
        results = model(frame, conf=0.25)

        for detection in results[0].boxes:
            x1, y1, x2, y2 = map(int, detection.xyxy[0])
            class_id = detection.cls[0]
            conf = detection.conf[0]

            # Draw bounding box and label
            cv2.rectangle(frame, (x1, y1), (x2, y2), (0, 255, 0), 2)
            cv2.putText(frame, f'{model.names[int(class_id)]} {conf:.2f}', (x1, y1 - 10), font, 0.75, (255, 255, 255), 1, cv2.LINE_AA)
            ret, encoded_frame = cv2.imencode('.jpg', frame)
            yield (b'--frame\r\n' b'Content-Type: image/jpeg\r\n\r\n' + bytearray(encoded_frame) + b'\r\n')


        # Wait for 'q' key to exit
        k = cv2.waitKey(1)
        if k == ord('q'):
            break

    # Release the camera and close all windows
    video_camera.release()
    cv2.destroyAllWindows()

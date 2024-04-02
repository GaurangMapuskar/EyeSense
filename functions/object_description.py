import cv2
import pathlib
import textwrap
from PIL import Image
import pyttsx3
import speech_recognition as sr
import google.generativeai as genai
from IPython.display import display, Markdown
import threading
from flask import redirect, url_for
from camera import VideoCamera

def object_description():
    r = sr.Recognizer()
    genai.configure(api_key='AIzaSyCxTQeZ2MKWOnBugK4MJFxdRF4XzM29Nl8')

    def to_markdown(text):
        text = text.replace('•', '  *')
        return Markdown(textwrap.indent(text, '> ', predicate=lambda _: True))

    model = genai.GenerativeModel('gemini-1.0-pro-vision-latest')
    font = cv2.FONT_HERSHEY_COMPLEX
    filename = "captured_image.jpg"

    def speech_recognition_thread():
        while True:
            try:
                with sr.Microphone() as source:
                    print("Listening...")
                    r.adjust_for_ambient_noise(source, duration=0.2)
                    audio = r.listen(source)
                    command = r.recognize_google(audio).lower()
                    print("You said:", command)
                    if command.startswith('describe'):
                        describe_image(command)
            except sr.RequestError as e:
                print("Could not request results; {0}".format(e))
            except sr.UnknownValueError:
                print("Unknown error occurred.")

    def describe_image(command):
        img = video_camera.get_frame()
        cv2.imwrite(filename, img)
        image = Image.open(filename)
        response = model.generate_content([command, image])
        response.resolve()
        description = response.text
        print(description)
        cv2.putText(img, description, (10, 30), font, 1, (255, 255, 255), 2, cv2.LINE_AA)
  

    # Create an instance of VideoCamera
    video_camera = VideoCamera()

    thread = threading.Thread(target=speech_recognition_thread)
    thread.daemon = True
    thread.start()

    while True:
        img = video_camera.get_frame()
        ret, encoded_frame = cv2.imencode('.jpg', img)
        yield (b'--frame\r\n' b'Content-Type: image/jpeg\r\n\r\n' + bytearray(encoded_frame) + b'\r\n')
        
        k = cv2.waitKey(1)
        if k == ord('q'):
            break

    if k == ord('q'):
        cv2.destroyAllWindows()
        return redirect(url_for('index'))

import threading
import cv2
from camera import VideoCamera
from flask import Flask, render_template, Response, request, redirect, url_for
from functions.currency_detection import currency_detection
from functions.face_detection import face_detection
from functions.object_description import object_description
from functions.object_detection import object_detection
import speech_recognition as sr

app = Flask(__name__) 
app.config['SERVER_NAME'] = 'localhost:5000'  # Replace with your server name and port
# app.config['APPLICATION_ROOT'] = '/myapp'  # Optional, if app runs under a subdirectory
# app.config['PREFERRED_URL_SCHEME'] = 'https'  

def voice_input():
    recognizer = sr.Recognizer()
    with sr.Microphone() as source:
        recognizer.adjust_for_ambient_noise(source)
        print("Listening for voice input...")
        with app.app_context():
            while True:
                audio = recognizer.listen(source)
                try:
                    command = recognizer.recognize_google(audio).lower()
                    print("Voice input:", command)
                    if 'face detection' in command:
                        return redirect(url_for('index', action='face_detection'))
                    elif 'object detection' in command:
                        return redirect(url_for('index', action='object_detection'))
                    elif 'currency detection' in command:
                        return redirect(url_for('index', action='currency_detection'))
                    elif 'object description' in command:
                        return redirect(url_for('index', action='object_description'))
                except sr.UnknownValueError:
                    print("Could not understand audio")
                except sr.RequestError as e:
                    print("Could not request results; {0}".format(e))

# Run the voice_input function in a separate thread
def start_voice_input():
    voice_thread = threading.Thread(target=voice_input)
    voice_thread.daemon = True
    voice_thread.start()

# Call the start_voice_input function before the first request
# @app.before_request
# def before_first_request_func():
#     start_voice_input()

# app.before_request_funcs = [(None, start_voice_input())]


@app.route('/')
def index(): 
    action = request.args.get('action')

    if action == 'object_detection':
        return render_template('object.html')
    elif action == 'currency_detection':
        return render_template('currency.html')
    elif action == 'object_description':
        return render_template('description.html')
    elif action == 'face_detection':
        return render_template('face.html')
    return render_template('index.html')
    
class VideoCamera(object):
    def __init__(self):
        self.video = cv2.VideoCapture(0)

    def __del__(self):
        self.video.release()

    def get_frame(self):
        ret, frame = self.video.read()

        ret, jpeg = cv2.imencode('.jpg', frame)
        return jpeg.tobytes()

def gen(camera):
    while True:
        frame = camera.get_frame()
        yield (b'--frame\r\n'
               b'Content-Type: image/jpeg\r\n\r\n' + frame + b'\r\n\r\n')
        
@app.route('/video_feed')
def video_feed():
    return Response(gen(VideoCamera()), mimetype='multipart/x-mixed-replace; boundary=frame')

@app.route('/currency_detection')
def currency():
    # render_template('currency.html')
    return Response(currency_detection(), mimetype='multipart/x-mixed-replace; boundary=frame')

@app.route('/object_description')
def description():
    return Response(object_description(), mimetype='multipart/x-mixed-replace; boundary=frame')

@app.route('/object_detection')
def object():
    return Response(object_detection(), mimetype='multipart/x-mixed-replace; boundary=frame')

@app.route('/face')
def face():
    return Response(face_detection(), mimetype='multipart/x-mixed-replace; boundary=frame')

@app.route('/contact')
def contact():
    return render_template('contact.html')

@app.route('/about')
def about():
    return render_template('about.html')



if __name__ == '__main__':
    start_voice_input()
    app.run(debug=True)

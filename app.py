import cv2
from camera import VideoCamera
from flask import Flask, render_template, Response, request
from functions.currency_detection import currency_detection
from functions.face_detection import face_detection
from functions.object_description import object_description
from functions.object_detection import object_detection

app = Flask(__name__) 

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
    app.run(debug=True)

from flask import Flask, render_template, Response, request
from functions.currency_detection import currency_detection
from functions.object_description import object_description
from functions.object_detection import object_detection

app = Flask(__name__)

@app.route('/')
def index(): 
    action = request.args.get('action')

    if action == 'object_detection':
        object_detection()
        return render_template('index.html')
        # return Response(object_detection(), mimetype='multipart/x-mixed-replace; boundary=frame')
    elif action == 'currency_detection':
        currency_detection()
        return render_template('index.html')
        # return Response(currency_detection(), mimetype='multipart/x-mixed-replace; boundary=frame')
    elif action == 'object_description':
        object_description()
        return render_template('index.html')
        # return Response(object_description(), mimetype='multipart/x-mixed-replace; boundary=frame')
    return render_template('index.html')
    

# @app.route('/video_feed')
# def video_feed():
#     action = request.args.get('action')

#     if action == 'object_detection':
#         return Response(object_detection(), mimetype='multipart/x-mixed-replace; boundary=frame')
#     elif action == 'currency_detection':
#         return Response(currency_detection(), mimetype='multipart/x-mixed-replace; boundary=frame')
#     elif action == 'object_description':
#         return Response(object_description(), mimetype='multipart/x-mixed-replace; boundary=frame')
#     else:
#         return "Invalid action"
    

@app.route('/contact')
def contact():
    return render_template('contact.html')

@app.route('/about')
def about():
    return render_template('about.html')

if __name__ == '__main__':
    app.run(debug=True)

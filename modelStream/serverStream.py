from flask import Flask,render_template,Response, stream_with_context
import cv2
import os
from model import predict_stream

app=Flask(__name__)


# @stream_with_context
# def generate_frames():
#     if os.environ.get('WERKZEUG_RUN_MAIN') or Flask.debug is False:
#         camera=cv2.VideoCapture(0)
#         print(camera.isOpened())
#         print('Yes camera')
#     else:
#         print('No camera')
#     while True:
#         ## read the camera frame
#         success,frame=camera.read()
#         if not success:
#             break
#         else:
#             ret,buffer=cv2.imencode('.jpg',frame)
#             frame=buffer.tobytes()

#         yield(b'--frame\r\n'
#                    b'Content-Type: image/jpeg\r\n\r\n' + frame + b'\r\n')


@app.route('/')
def index():
    return render_template('index.html')

@app.route('/video')
def video():
    return Response(predict_stream("video/Чемпионат Мира 2019 — Инцелль - Мужчины 500.mp4"),mimetype='multipart/x-mixed-replace; boundary=frame')

if __name__=="__main__":
    app.run(debug=True, host="0.0.0.0", port=7000)
    
    # if os.environ.get('WERKZEUG_RUN_MAIN') or Flask.debug is False:
    #     camera.release()

# import main Flask class and request object
import base64
import json
import os
import cv2
from flask import Flask, Response, render_template, request, stream_with_context
from moviepy.editor import VideoFileClip
from model import predict_video


# create the Flask app
app = Flask(__name__)

video_path = 'videos/video.avi'
gif_path = 'gifs/out.gif'

@stream_with_context
def generate_frames():
    
    
    if os.environ.get('WERKZEUG_RUN_MAIN') or Flask.debug is False:
        camera=cv2.VideoCapture(video_path)
        #camera=cv2.VideoCapture(0)
        #camera=cv2.VideoCapture('gifs/out.gif')
        print(camera.isOpened())
        print('Yes camera')
    else:
        print('No camera')
    
    
    while True:
        ## read the camera frame
        
        success,frame=camera.read()
        if not success:
            break
        else:
            ret,buffer=cv2.imencode('.jpg',frame)
            frame=buffer.tobytes()

        yield(b'--frame\r\n'
                   b'Content-Type: image/jpeg\r\n\r\n' + frame + b'\r\n')
    camera.release()

@app.route('/video')
def video():
    return Response(generate_frames(),mimetype='multipart/x-mixed-replace; boundary=frame')

def decodeVideo(b64):
    #json->video
    fh = open(video_path, "wb")
    fh.write(base64.b64decode(b64))
    fh.close()

def encodeGIF():
    b64 = ''
    with open(gif_path, "rb") as videoFile:
        text = base64.b64encode(videoFile.read())
        b64 = str(text)[2:-1]
    b64 = "data:image/gif;base64,"+b64
    return b64

@app.route('/upload',methods=["POST"])
def query_example():
    content_type = request.headers.get('Content-Type')
    if (content_type == 'application/json'):
        data = request.json
        #сохраняем видео
        decodeVideo(data.get('b64'))
        #модель
        answer = predict_video(video_path)

        #сохраняем gif
        vc = VideoFileClip("videos/video.avi")
        vc.write_gif(gif_path)
        print(data.get("name"))
        modelclass = {'class': answer,'b64':encodeGIF(),'videoName':data.get("name")}

        modelclass = json.dumps(modelclass)
        return modelclass
    else:
        return "Content type is not supported"

@app.route('/')
def html():
    return render_template('application/json')

if __name__ == '__main__':
    # run app in debug mode on port 5000
    app.run(debug=True, host="0.0.0.0", port=5000)
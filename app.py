import socket
import ssl

import cv2
import numpy as np
import pyautogui
from flask import Flask, redirect, request, render_template, Response
from flask_sslify import SSLify

host = socket.gethostbyname(socket.gethostname())
app = Flask(__name__)
sslify = SSLify(app)


@app.before_request
def force_https():
    if not request.is_secure:
        url = request.url.replace('http://', 'https://', 1)
        return redirect(url, code=301)


@app.route('/')
def index():
    return render_template('index.html')


def generate_frames(camera_index):
    camera = cv2.VideoCapture(camera_index)  # 打开摄像头，参数0表示默认摄像头
    while True:
        success, frame = camera.read()  # 读取摄像头帧
        if not success:
            break
        ret, buffer = cv2.imencode('.jpg', frame)  # 将帧编码为JPEG图像
        frame = buffer.tobytes()  # 将图像转换为字节串
        yield (b'--frame\r\n'
               b'Content-Type: image/jpeg\r\n\r\n' + frame + b'\r\n')  # 生成帧数据
    camera.release()


@app.route('/video_feed/<int:camera_index>')
def video_feed(camera_index):
    return Response(generate_frames(camera_index), mimetype='multipart/x-mixed-replace; boundary=frame')


@app.route('/server')
def server_():
    camera_index = request.args.get('c', default='0', type=int)
    camera_rotate = request.args.get('r', default='0', type=int)
    return render_template('server/index.html', selected_camera=camera_index, camera_rotate=camera_rotate)  # 将相机列表传递到模板中


def screen():
    while True:
        # 截屏
        screenShotImg = pyautogui.screenshot()
        screenShotImg = cv2.cvtColor(np.array(screenShotImg), cv2.COLOR_RGB2BGR)
        # 获取鼠标位置
        mouseX, mouseY = pyautogui.position()
        # 在图像上绘制鼠标
        cv2.circle(screenShotImg, (mouseX, mouseY), 5, (0, 255, 0), -1)
        # 转换图像格式并发送给前端
        _, frame = cv2.imencode('.JPEG', screenShotImg)
        frame = frame.tobytes()
        yield (b'--frame\r\n Content-Type: image/jpeg\r\n\r\n' + frame)


@app.route('/screen_sharing')
def video_fed():
    # 分帧推送截屏图像数据到前端
    return Response(screen(), mimetype='multipart/x-mixed-replace; boundary=frame')


@app.route('/client')
def client():
    camera_rotate = request.args.get('r', default='0', type=int)
    return render_template('client/index.html', camera_rotate=camera_rotate)


@app.route('/favicon.ico')
def favicon():
    return Response('', status=200)


if __name__ == '__main__':
    context = ssl.SSLContext(ssl.PROTOCOL_TLS_SERVER)
    context.load_cert_chain('./cert.pem', './key.pem')  # 替换为你的证书和私钥路径
    app.run(host=host, port=2024, ssl_context=context, debug=True)

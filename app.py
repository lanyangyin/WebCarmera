import cv2
from flask import Flask, redirect, request, render_template, Response
from flask_sslify import SSLify
import ssl

app = Flask(__name__)
sslify = SSLify(app)


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


@app.route('/client')
def client():
    return render_template('client/index.html')


@app.route('/favicon.ico')
def favicon():
    return Response('', status=200)


@app.before_request
def force_https():
    if not request.is_secure:
        url = request.url.replace('http://', 'https://', 1)
        return redirect(url, code=301)


if __name__ == '__main__':
    context = ssl.SSLContext(ssl.PROTOCOL_TLS_SERVER)
    context.load_cert_chain('./cert.pem', './key.pem')  # 替换为你的证书和私钥路径
    app.run(host='localhost', port=2040, ssl_context=context, debug=True)

import getopt
import socket
import ssl
import sys

import cv2
import numpy as np
import pyautogui
from flask import Flask, redirect, request, render_template, Response
from flask_sslify import SSLify

try:
    opts, args = getopt.getopt(sys.argv[1:], "h:p:", ['host=', 'port='])
except:
    opts = []


def get_local_ip_addresses():
    ip_addresses = []
    # 获取本地主机名
    hostname = socket.gethostname()
    try:
        # 获取主机名对应的所有IP地址
        ip_addresses = socket.gethostbyname_ex(hostname)[-1]
    except socket.gaierror:
        pass
    ip_addresses.append("127.0.0.1")
    ip_addresses.append("localhost")
    return ip_addresses

def get_host():
    host = '0'
    ip_addresses = get_local_ip_addresses()
    for op, value in opts:
        if op in ("-h", "--host"):
            host = value.strip()
    if host in ip_addresses:
        return host
    else:
        host = socket.gethostbyname(socket.gethostname())
        if host.endswith(".1"):
            for host in ip_addresses:
                if not host.endswith(".1") and host != "localhost":
                    return host
        else:
            return host
    return "127.0.0.1"

def find_unused_port():
    port = 1881
    for op, value in opts:
        if op in ("-p", "--port"):
            try:
                port = int(value.strip())
            except:
                port = 1881

    def is_port_in_use(port):
        """
        判断port是否被占用
        :param port:
        :return:
        """
        with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
            try:
                s.bind(("localhost", port))
            except socket.error:
                return True
            return False

    if is_port_in_use(port):
        port = 1881
        if is_port_in_use(port):
            # 创建一个临时socket
            temp_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            temp_socket.bind(('localhost', 0))  # 绑定到本地任意可用端口
            _, port = temp_socket.getsockname()  # 获取分配的端口
            temp_socket.close()  # 关闭socket
    return port


host = get_host()
port = find_unused_port()
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
    # for ip in get_local_ip_addresses():
    #     print(ip)
    app.run(host=host, port=port, ssl_context=context, debug=True)


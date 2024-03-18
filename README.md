# WebCarmera

## 用于在浏览器中调用用户设备和服务器端的摄像头

### 这里有三个不同的 OpenSSL 命令，用于生成 SSL/TLS 证书和密钥。让我们逐个解释每个命令的参数：

```bash
openssl req -newkey rsa:2048 -new -nodes -x509 -days 3650 -keyout key.pem -out cert.pem
```

- req: 这个命令告诉 OpenSSL 执行证书请求 (CSR - Certificate Signing Request) 相关的操作。
- newkey rsa:2048: 这个选项告诉 OpenSSL 生成一个新的 RSA 密钥对，其中 RSA 密钥的长度为 2048 位。
- new: 告诉 OpenSSL 创建一个新的证书请求。
- nodes: 这个选项告诉 OpenSSL 在生成密钥时不使用加密。如果使用了这个选项，生成的密钥文件将不会有密码保护。
- x509: 这个选项告诉 OpenSSL 生成自签名的 X.509 格式证书。
- days 3650: 这个选项指定证书的有效期限，以天为单位。在这个例子中，证书的有效期为 3650 天，大约是 10 年。
- keyout key.pem: 指定生成的私钥文件的输出路径和名称。
- out cert.pem: 指定生成的证书文件的输出路径和名称。

```bash
openssl req -newkey rsa:2048 -new -nodes -keyout key.pem -out csr.pem
```

这个命令也是用于创建证书请求 (CSR)。

- keyout key.pem: 这个选项指定生成的私钥文件的输出路径和名称。
- out csr.pem: 这个选项指定生成的证书请求文件的输出路径和名称。

```bash
openssl req -x509 -newkey rsa:4096 -nodes -out cert.pem -keyout key.pem -days 365
```

这个命令也是用于生成自签名的 X.509 格式证书。

- days 365: 这个选项指定证书的有效期限为 365 天，即一年。
- newkey rsa:4096: 这个选项告诉 OpenSSL 生成一个新的 RSA 密钥对，其中 RSA 密钥的长度为 4096 位。
- keyout key.pem: 指定生成的私钥文件的输出路径和名称。
- out cert.pem: 指定生成的证书文件的输出路径和名称。
  总的来说，这些命令都是用于生成 SSL/TLS 证书和密钥。第一个命令生成自签名的 X.509 格式证书，而第二个和第三个命令生成证书请求 (CSR)，这些请求可以发送给证书颁发机构 (CA) 进行签名，或者用于创建自签名证书。

### 使用证书和私钥在app.py开启https

```python
    context = ssl.SSLContext(ssl.PROTOCOL_TLS_SERVER)
    context.load_cert_chain('./cert.pem', './key.pem')  # 替换为你的证书和私钥路径
    app.run(host='localhost', port=port, ssl_context=context, debug=True)
```

# 使用

- https://host:port/server?c=int: 相机编号&r=int：旋转角度
- https://host:port/client?r=int：旋转角度

# 参考

## https服务

- [Python3开启自带http服务](https://blog.csdn.net/SPACESTUDIO/article/details/86760104)
- [Python实现本地电脑启动HTTP服务](https://blog.csdn.net/songpeiying/article/details/131637405)
- [Flask: 如何给Python Flask Web服务器添加HTTPS功能](https://geek-docs.com/flask/flask-questions/4_flask_can_you_add_https_functionality_to_a_python_flask_web_server.html#:~:text=Flask:%20%E5%A6%82%E4%BD%95%E7%BB%99Python%20Flask%20Web%E6%9C%8D%E5%8A%A1%E5%99%A8%E6%B7%BB%E5%8A%A0HTTPS%E5%8A%9F%E8%83%BD%201%20%E4%BB%80%E4%B9%88%E6%98%AFHTTPS%EF%BC%9F%20HTTPS%E6%98%AFHTTP%E7%9A%84%E5%AE%89%E5%85%A8%E7%89%88%E6%9C%AC%EF%BC%8C%E5%AE%83%E4%BD%BF%E7%94%A8SSL%EF%BC%88Secure%20Sockets,%20%E5%A6%82%E6%9E%9C%E6%88%91%E4%BB%AC%E6%83%B3%E8%A6%81%E5%BC%BA%E5%88%B6%E6%89%80%E6%9C%89%E8%AF%B7%E6%B1%82%E9%83%BD%E4%BD%BF%E7%94%A8HTTPS%EF%BC%8C%E6%97%A0%E8%AE%BA%E6%98%AF%E5%9C%A8%E6%9C%AC%E5%9C%B0%E5%BC%80%E5%8F%91%E8%BF%98%E6%98%AF%E7%94%9F%E4%BA%A7%E7%8E%AF%E5%A2%83%E4%B8%AD%EF%BC%8C%E6%88%91%E4%BB%AC%E5%8F%AF%E4%BB%A5%E4%BD%BF%E7%94%A8%20app.before_request%20%E8%A3%85%E9%A5%B0%E5%99%A8%E6%9D%A5%E5%AE%9E%E7%8E%B0%E8%BF%99%E4%B8%80%E7%82%B9%EF%BC%9A%20...%206%20%E4%BD%BF%E7%94%A8Nginx%E4%BB%A3%E7%90%86%E6%9C%8D%E5%8A%A1%E5%99%A8%20...%20%E6%9B%B4%E5%A4%9A%E9%A1%B9%E7%9B%AE)
- [python3搭https服务](https://blog.csdn.net/junbujianwpl/article/details/104405552)

## 调用摄像头

- [html5调用摄像头功能](https://segmentfault.com/a/1190000014741852)
- [cv2.VideoCapture读取视频或摄像头，并进行保存帧图像或视频](https://blog.csdn.net/weixin_40922285/article/details/102967331)
- [树莓派/PC实现实时摄像头数据共享—最优方法（搭建网络摄像头）](https://cloud.tencent.com/developer/article/1775772)
- [opencv python 调用网络摄像头 （局域网）](https://blog.csdn.net/weixin_40959890/article/details/114527379)
- [python 通过socket通讯实现实时摄像头视频传输](https://blog.csdn.net/dabo_520/article/details/129941397)
- [python 传输摄像头](https://blog.51cto.com/u_16213300/8745574#:~:text=Python%20%E4%BC%A0%E8%BE%93%E6%91%84%E5%83%8F%E5%A4%B4%E5%AE%9E%E7%8E%B0%E6%95%99%E7%A8%8B%201%201.%E6%95%B4%E4%BD%93%E6%B5%81%E7%A8%8B%20%E4%B8%BA%E4%BA%86%E5%AE%9E%E7%8E%B0Python%E4%BC%A0%E8%BE%93%E6%91%84%E5%83%8F%E5%A4%B4%E7%9A%84%E5%8A%9F%E8%83%BD%EF%BC%8C%E6%88%91%E4%BB%AC%E5%8F%AF%E4%BB%A5%E6%8C%89%E7%85%A7%E4%BB%A5%E4%B8%8B%E6%AD%A5%E9%AA%A4%E8%BF%9B%E8%A1%8C%E6%93%8D%E4%BD%9C%EF%BC%9A%20%E6%8E%A5%E4%B8%8B%E6%9D%A5%EF%BC%8C%E6%88%91%E4%BB%AC%E5%B0%86%E9%80%90%E6%AD%A5%E8%AE%B2%E8%A7%A3%E6%AF%8F%E4%B8%AA%E6%AD%A5%E9%AA%A4%E9%9C%80%E8%A6%81%E8%BF%9B%E8%A1%8C%E7%9A%84%E6%93%8D%E4%BD%9C%E3%80%822%202.%E4%BB%A3%E7%A0%81%E7%A4%BA%E4%BE%8B%20%E4%B8%8B%E9%9D%A2%E6%98%AF%E4%B8%80%E4%B8%AA%E5%AE%8C%E6%95%B4%E7%9A%84%E4%BB%A3%E7%A0%81%E7%A4%BA%E4%BE%8B%EF%BC%8C%E7%94%A8%E4%BA%8E%E5%AE%9E%E7%8E%B0Python%E4%BC%A0%E8%BE%93%E6%91%84%E5%83%8F%E5%A4%B4%E5%8A%9F%E8%83%BD%EF%BC%9A%20...4%204.%E7%94%98%E7%89%B9%E5%9B%BE%20%E4%B8%8B%E9%9D%A2%E6%98%AF%E4%B8%80%E4%B8%AA%E4%BD%BF%E7%94%A8%E7%94%98%E7%89%B9%E5%9B%BE%E8%A1%A8%E6%98%BE%E7%A4%BA%E7%9A%84%E4%BB%BB%E5%8A%A1%E6%97%B6%E9%97%B4%E5%AE%89%E6%8E%92%EF%BC%9A)
- [html5+JS调用摄像头示例](https://blog.csdn.net/cnds123/article/details/122515662)
- [利用HTML5 MediaDevices API调用手机摄像头并结合JavaScript库实现人脸识别](https://segmentfault.com/a/1190000044698126)
- [Web调用电脑摄像头【实时画面、拍照、截图】](https://blog.csdn.net/qq_45021180/article/details/111561634)
- [Django OpenCV 在 Django 网页中实时从摄像头进行视频流](https://deepinout.com/django/django-questions/707_django_opencv_live_stream_from_camera_in_django_webpage.html)
- [Python实现网页端显示摄像头拍摄视频](https://blog.csdn.net/private_void_main/article/details/89598006)
- [JS获取电脑摄像头，麦克风，点击切换摄像头设备](https://blog.csdn.net/qq_36947128/article/details/118526979)
- [前端调取摄像头并实现拍照功能](https://zhuanlan.zhihu.com/p/661985982)
- [如何使用JavaScript访问设备摄像头（前后）](https://cloud.tencent.com/developer/article/1641490)

## 屏幕共享

- [python flask 实现电脑屏幕实时共享\_python flask 直播电脑桌面-CSDN博客](https://blog.csdn.net/MAILLIBIN/article/details/126742575)
- [前端 - 基于 Web 端的屏幕共享实践 - ZEGO即构科技 - SegmentFault 思否](https://segmentfault.com/a/1190000040512445)
- [基于python实现屏幕共享\_python创建屏幕共享-CSDN博客](https://blog.csdn.net/weixin_41761542/article/details/118381109)

## 实例

- [使用 Chrome、Safari 或 Firefox 的在线二维码扫描相机](https://online-qr-scanner.net/zh-cn/camera.html)
- [纯H5实现扫一扫功能，亲测PC和手机端可用](https://www.jianshu.com/p/c84a0135824b)
- [推流进阶 (zegodev.github.io)](https://zegodev.github.io/zego-express-webrtc-sample/screen/index.html)

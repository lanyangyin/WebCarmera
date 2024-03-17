# WebCarmera
用于在浏览器中调用用户设备和服务器端的摄像头



这里有三个不同的 OpenSSL 命令，用于生成 SSL/TLS 证书和密钥。让我们逐个解释每个命令的参数：

openssl req -newkey rsa:2048 -new -nodes -x509 -days 3650 -keyout key.pem -out cert.pem

req: 这个命令告诉 OpenSSL 执行证书请求 (CSR - Certificate Signing Request) 相关的操作。
-newkey rsa:2048: 这个选项告诉 OpenSSL 生成一个新的 RSA 密钥对，其中 RSA 密钥的长度为 2048 位。
-new: 告诉 OpenSSL 创建一个新的证书请求。
-nodes: 这个选项告诉 OpenSSL 在生成密钥时不使用加密。如果使用了这个选项，生成的密钥文件将不会有密码保护。
-x509: 这个选项告诉 OpenSSL 生成自签名的 X.509 格式证书。
-days 3650: 这个选项指定证书的有效期限，以天为单位。在这个例子中，证书的有效期为 3650 天，大约是 10 年。
-keyout key.pem: 指定生成的私钥文件的输出路径和名称。
-out cert.pem: 指定生成的证书文件的输出路径和名称。
openssl req -newkey rsa:2048 -new -nodes -keyout key.pem -out csr.pem

这个命令也是用于创建证书请求 (CSR)。
-keyout key.pem: 这个选项指定生成的私钥文件的输出路径和名称。
-out csr.pem: 这个选项指定生成的证书请求文件的输出路径和名称。
openssl req -x509 -newkey rsa:4096 -nodes -out cert.pem -keyout key.pem -days 365

这个命令也是用于生成自签名的 X.509 格式证书。
-days 365: 这个选项指定证书的有效期限为 365 天，即一年。
-newkey rsa:4096: 这个选项告诉 OpenSSL 生成一个新的 RSA 密钥对，其中 RSA 密钥的长度为 4096 位。
-keyout key.pem: 指定生成的私钥文件的输出路径和名称。
-out cert.pem: 指定生成的证书文件的输出路径和名称。
总的来说，这些命令都是用于生成 SSL/TLS 证书和密钥。第一个命令生成自签名的 X.509 格式证书，而第二个和第三个命令生成证书请求 (CSR)，这些请求可以发送给证书颁发机构 (CA) 进行签名，或者用于创建自签名证书。

load_cert_chain('./cert.pem', './key.pem')  # 替换为你的证书和私钥路径

参考
https服务
[Python3开启自带http服务](https://blog.csdn.net/SPACESTUDIO/article/details/86760104)
[Python实现本地电脑启动HTTP服务](https://blog.csdn.net/songpeiying/article/details/131637405)
https://blog.csdn.net/junbujianwpl/article/details/104405552
https://geek-docs.com/flask/flask-questions/4_flask_can_you_add_https_functionality_to_a_python_flask_web_server.html#:~:text=Flask: 如何给Python Flask Web服务器添加HTTPS功能 1 什么是HTTPS？ HTTPS是HTTP的安全版本，它使用SSL（Secure Sockets, 如果我们想要强制所有请求都使用HTTPS，无论是在本地开发还是生产环境中，我们可以使用 app.before_request 装饰器来实现这一点： ... 6 使用Nginx代理服务器 ... 更多项目



调用摄像头
https://segmentfault.com/a/1190000014741852
https://blog.csdn.net/cnds123/article/details/122515662
[cv2.VideoCapture读取视频或摄像头，并进行保存帧图像或视频](https://blog.csdn.net/weixin_40922285/article/details/102967331)https://blog.csdn.net/weixin_40922285/article/details/102967331
[树莓派/PC实现实时摄像头数据共享—最优方法（搭建网络摄像头）](https://cloud.tencent.com/developer/article/1775772)https://cloud.tencent.com/developer/article/1775772
[opencv python 调用网络摄像头 （局域网）](https://blog.csdn.net/weixin_40959890/article/details/114527379)https://blog.csdn.net/weixin_40959890/article/details/114527379
[python 通过socket通讯实现实时摄像头视频传输](https://blog.csdn.net/dabo_520/article/details/129941397)https://blog.csdn.net/dabo_520/article/details/129941397
[python 传输摄像头](https://blog.51cto.com/u_16213300/8745574#:~:text=Python传输摄像头实现教程 1 1. 整体流程 为了实现Python传输摄像头的功能，我们可以按照以下步骤进行操作： 接下来，我们将逐步讲解每个步骤需要进行的操作。 2 2. 代码示例 下面是一个完整的代码示例，用于实现Python传输摄像头功能： ... 4 4. 甘特图 下面是一个使用甘特图表显示的任务时间安排：)https://blog.51cto.com/u_16213300/8745574#:~:text=Python传输摄像头实现教程 1 1. 整体流程 为了实现Python传输摄像头的功能，我们可以按照以下步骤进行操作： 接下来，我们将逐步讲解每个步骤需要进行的操作。 2 2. 代码示例 下面是一个完整的代码示例，用于实现Python传输摄像头功能： ... 4 4. 甘特图 下面是一个使用甘特图表显示的任务时间安排：
[html5+JS调用摄像头示例](https://blog.csdn.net/cnds123/article/details/122515662)https://blog.csdn.net/cnds123/article/details/122515662
[利用HTML5 MediaDevices API调用手机摄像头并结合JavaScript库实现人脸识别](https://segmentfault.com/a/1190000044698126)https://segmentfault.com/a/1190000044698126
[Web调用电脑摄像头【实时画面、拍照、截图】](https://blog.csdn.net/qq_45021180/article/details/111561634)https://blog.csdn.net/qq_45021180/article/details/111561634
[Django OpenCV 在 Django 网页中实时从摄像头进行视频流](https://deepinout.com/django/django-questions/707_django_opencv_live_stream_from_camera_in_django_webpage.html)https://deepinout.com/django/django-questions/707_django_opencv_live_stream_from_camera_in_django_webpage.html
[Python实现网页端显示摄像头拍摄视频](https://blog.csdn.net/private_void_main/article/details/89598006)https://blog.csdn.net/private_void_main/article/details/89598006















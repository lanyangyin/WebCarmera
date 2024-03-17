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


import socket               # 导入 socket 模块
import time
import os
s = socket.socket()         # 创建 socket 对象
host = socket.gethostname() # 获取本地主机名
port = 20500                # 设置端口
s.bind((host, port))        # 绑定端口

s.listen(128)                 # 等待客户端连接
i=0
def file_deal(file_name):
    files = open(file_name, "rb")
    mes = files.read()
    return mes

while True:
    c, addr = s.accept()     # 建立客户端连接。
    mes = file_deal("test.jpg")
    size = os.path.getsize("test.jpg")
    size1=str(size)#encoda只接受str类型
    c.send(size1.encode())
    time.sleep(0.5)
    if mes:
        # 如果文件不为空发送
        print(mes)
        c.send(mes)
        print(1)



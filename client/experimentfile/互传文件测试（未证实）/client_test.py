import socket
import os,time

# 创建 socket 对象
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# 获取本地主机名
host = socket.gethostname()

# 设置端口号
port = 20500

# 连接服务，指定主机和端口
s.connect((host, port))
file_name="123.jpg"
# 接收小于 1024 字节的数据
new_file = open(file_name, "wb")
while 1:
    time.sleep(5)
    s.send("S".encode('utf-8'))

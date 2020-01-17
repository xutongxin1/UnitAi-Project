#导入必要包
import json
import socket
from socket import *
#导入自定义函数

#内函数


#建立连接
listen_socket = socket(AF_INET, SOCK_STREAM)
   # 设置允许复用地址,当建立连接之后服务器先关闭，设置地址复用
    # 设置socket层属性    复用地址    允许
listen_socket.setsockopt(SOL_SOCKET, SO_REUSEADDR, 1)
    # 设置listen_socket为非阻塞方式
listen_socket.setblocking(False)  # 设置非阻塞

while True:
    connect_socket, addr = listen_socket.accept()
    while True:
            recv_data = connect_socket.recv(1024)
            if len(recv_data) == 0:
                connect_socket.close()
                print("off")
            else:
                print(recv_data)

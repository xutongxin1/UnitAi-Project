import json
import socket,os,hashlib,time
from threading import Thread
#导入自定义函数
#建立连接
s = socket.socket()         # 创建 socket 对象
host = socket.gethostname() # 获取本地主机名
port = 11171            # 设置端口
s.bind((host, port))        # 绑定端口
s.listen(5)                 # 等待客户端连接
def receive_service(c):
    #验证身份
    print(1)
    msg1 = c.recv(1024)
    msg = msg1.decode('utf-8')
    print(2)
    result = json.loads(msg)
    if (result["apikey"] == 0):
        c.send("A".encode('utf-8'))
        print("Access denine")  # 数据库校验
        c.close()
        return
    print(result)
    c.send("O".encode('utf-8'))

    #确认文件,发送大小头
    path=result["filename"]
    if os.path.exists(path):
        size = str(os.path.getsize(path))
        f = open(path, 'rb')
        myHash = hashlib.md5()
        while True:
            d = f.read(8096)
            if not d:
                break
            myHash.update(d)
        md5 = myHash.hexdigest()
        head = {
            "size": size,
            "md5": md5,
            }
        head = json.dumps(head)
        s.send(head.encode('utf-8'))
        time.sleep(0.5)

        #发送文件
        file = open(path, 'rb')
        f = file.read()
        block = float(int(os.path.getsize(path)) / 1024)
        if (block % 1 != 0):
            block = int(block + 1)
        i = 1
        t = 0
        while i <= block:
            s.send(f[t:t + 1025])
            t += 1024
        print("sendsuccess")
        time.sleep(3)
        c.close()
        return

    else:
        c.send("N".encode('utf-8'))
        c.close()
        return

while True:
    c, client_addr = s.accept()
    #thread_do_service = Thread(target=receive_service, args=(connect_socket,))
    #thread_do_service.start()
    # 验证身份
    print(1)
    msg1 = c.recv(1024)
    msg = msg1.decode('utf-8')
    print(2)
    result = json.loads(msg)
    if (result["apikey"] == 0):
        c.send("A".encode('utf-8'))
        print("Access denine")  # 数据库校验
        c.close()
    print(result)
    c.send("O".encode('utf-8'))

    # 确认文件,发送大小头
    path = result["filename"]
    if os.path.exists(path):
        size = str(os.path.getsize(path))
        f = open(path, 'rb')
        myHash = hashlib.md5()
        while True:
            d = f.read(8096)
            if not d:
                break
            myHash.update(d)
        md5 = myHash.hexdigest()
        head = {
            "size": size,
            "md5": md5,
        }
        head = json.dumps(head)
        s.send(head.encode('utf-8'))
        time.sleep(0.5)

        # 发送文件
        file = open(path, 'rb')
        f = file.read()
        block = float(int(os.path.getsize(path)) / 1024)
        if (block % 1 != 0):
            block = int(block + 1)
        i = 1
        t = 0
        while i <= block:
            s.send(f[t:t + 1025])
            t += 1024
        print("sendsuccess")
        time.sleep(3)
        c.close()

    else:
        c.send("N".encode('utf-8'))
        c.close()


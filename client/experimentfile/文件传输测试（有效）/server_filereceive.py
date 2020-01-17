#导入必要包
import json
import socket
import hashlib,os
#导入自定义函数

#内函数


#建立连接
s = socket.socket()         # 创建 socket 对象
host = socket.gethostname() # 获取本地主机名
port = 11170             # 设置端口
s.bind((host, port))        # 绑定端口
s.listen(5)                 # 等待客户端连接
while True:
    c, addr = s.accept()
    print(1)
    msg1 = c.recv(1024)
    msg = msg1.decode('utf-8')
    print(2)
    result = json.loads(msg)
    if (result["apikey"] == 0):
        c.send("A".encode('utf-8'))
        print("Access denine")  # 数据库校验
        c.close()
        break
    print(result)
    c.send("O".encode('utf-8'))
    size = result["size"]
    msga = c.recv(size + 10)
    os.chdir(r'E:\UnitAi-Project\tmp')
    w = open(result["filename"], "wb")
    w.write(msg)
    w.close()
    f = open(result["filename"], 'rb')  # 校验
    md5_obj = hashlib.md5()
    while True:
        d = f.read(8096)
        if not d:
            break
        md5_obj.update(d)
    hash_code = md5_obj.hexdigest()
    f.close()
    md5 = str(hash_code).lower()
    if (result["md5"] == md5):
        print("Success")
        c.send("C".encode('utf-8'))
    else:
        print("Error")
        c.send("E".encode('utf-8'))
    c.close()
    #try:     # 建立客户端连接。


    #except:
        #print("No client")
        #c.close()

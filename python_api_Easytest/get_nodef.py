import socket
print("非函数版get构建")
file=open("./out.py", 'wb')
print("输入地址")
url=input()
file.write(("url='"+url+"'\n").encode("utf-8"))
file.write("headers = {'Content-Type': 'application/json'}".encode("utf-8"))
file.write("req = requests.get(urlcheck, headers)\n	result = json.loads(req.text)".encode("utf-8"))
file.close()
print("完成")
    




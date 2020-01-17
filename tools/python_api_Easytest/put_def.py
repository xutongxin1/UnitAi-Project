import socket
print("函数版put构建")
file=open("./out.py", 'wb')
print("函数名")
name=input()
print("输入地址")
url=input()
str="def "+name+"():\n"
file.write(str.encode("utf-8"))
file.write(("	url='"+url+"'\n").encode("utf-8"))
print("输入文件完整路径")
wh=input()
file.write('	file=open("'+wh+'", 'rb')'.encode("utf-8"))
file.write("	req = requests.put(urlupload,files=file)\n	result = json.loads(req.text)".encode("utf-8"))
file.write("}".encode("utf-8"))
file.close()
print("完成")
    




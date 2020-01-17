import socket
print("非函数版post构建")
file=open("./test.py", 'wb')
print("输入头")
print("默认application/json")
headers=input()
if len(headers)==0:
	headers="application/json"
print("输入地址")
url=input()
file.write(("url='"+url+"'\n").encode("utf-8"))
str="headers = {'Content-Type':'"+headers+"'}\n"
file.write(str.encode("utf-8"))
file.write("date={\n".encode("utf-8"))

print("输入其他项目，以回车结束")
t=0
while 1:
	print("输入对象名")
	name=input()
	if len(name)==0:
		break
	if t!=0:
		file.write(",\n".encode("utf-8"))
	print("输入对象值")
	val=input()
	t+=1
	file.write(("	'"+name+"'='"+val+"'").encode("utf-8"))
file.write("\n	}\n".encode("utf-8"))
file.write("req = requests.post(urlbegin, json.dumps(data_begin), headers)\nresult = json.loads(req.text)".encode("utf-8"))
file.close()
print("完成")
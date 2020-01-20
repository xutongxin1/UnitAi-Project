import socket,json,time,os
s = socket.socket()
host = socket.gethostname()
s.connect((host, 11171))
key="123321"
filename=input()
head = {
                    "apikey": key,
                    "filename": filename,
                }
print(head)
head=json.dumps(head)
s.send(head.encode('utf-8'))
time.sleep(1)
msg1=s.recv(1)
msg=msg1.decode('utf-8')
if msg=="A":
    print("No")
else:
    msg1 = s.recv(1024)
    msg = msg1.decode('utf-8')
    result = json.loads(msg)
    md5=result["md5"]
    print(md5)
    size=result["size"]
    os.chdir(r'D:\tmp')
    w = open(result["filename"], "wb")
    w.write(msg)
    w.close()


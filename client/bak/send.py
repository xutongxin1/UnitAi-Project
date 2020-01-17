# code:utf-8
Version="0.0.1b"
import socket,requests,json
import hashlib,time,os,configparser
from threading import Thread
#登录中枢
def hash(word):
    sha256 = hashlib.sha256()
    sha256.update(word.encode('utf-8'))
    res = sha256.hexdigest()
    return res
def login(acc,pd):
    curpath = os.path.dirname(os.path.realpath(__file__))
    cfgpath = os.path.join(curpath, "config/user.ini")
    conf = configparser.ConfigParser()
    conf.read(cfgpath, encoding="utf-8")
    add = conf.get("server", "add")
    port = conf.get("server", "port")
    #loginmode = conf.get("acc", "loginmode")
    pd = conf.get("acc", "pd")
    headers = {'Content-Type': 'application/json'}
    url="http://"+add+':'+port+"/login"
    print(url)
    pd=hash(pd)
    data = {
            "acc":acc,
            "pd":pd
    }
    req = requests.post(url, json.dumps(data), headers=headers)
    result = json.loads(req.text)
    print(result['code'])
    return result['code']

def login_old(acc,pd):
    curpath = os.path.dirname(os.path.realpath(__file__))
    cfgpath = os.path.join(curpath, "config/user.ini")
    conf = configparser.ConfigParser()
    conf.read(cfgpath, encoding="utf-8")
    #add = conf.get("server", "add")
    port = conf.get("server", "port")
    loginmode = conf.get("acc", "loginmode")
    pd = conf.get("acc", "pd")
    s = socket.socket()
    host = socket.gethostname()
    #print(host)
    port = int(port)
    print(port)
    #try:
    if True:
        s.connect((host, port))  # ip和端口

        # 以下为建立tcp连接


        if acc=='ConnectTest':
            s.send(acc.encode('utf-8'))
            msg1 = s.recv(10)
            so = msg1.decode('utf-8')
            s.close()
            print(so)
            return so
        s.send(acc.encode('utf-8'))
        time.sleep(1)
        if loginmode ==0:
            sha256 = hashlib.sha256()
            sha256.update(pd.encode('utf-8'))
            res = sha256.hexdigest()
        else:
            res=pd
        s.send(res.encode('utf-8'))
        time.sleep(1)
        msg1 = s.recv(1)
        so = msg1.decode('utf-8')
        s.close()

        if (so == "S"):
            return 0
        elif(so=="A"):
            return 2
        else:
            return 1

        # login触发事件
    #except:
        #print("No server")
        #return -1

#发送文件函数
#标准文件发送函数(带检查，全加载式检查文件，不带进度，适用于10m以下）
def sendfile1(ip,port,head,whfile):
    s = socket.socket()
    ip = socket.gethostname()
    print(ip)
    print(port)
    s.connect((ip, port))
    print(1)
    s.send(head.encode('utf-8'))
    time.sleep(0.5)
    msg1 = s.recv(1)
    msg = msg1.decode('utf-8')
    while 1:
        if (msg == "A"):
            print("Access denine")
            s.close()
            return 1
        elif (msg == "O"):
            file = open(whfile, 'rb')
            f=file.read()
            s.send(f)
            time.sleep(0.5)
            msg1 = s.recv(1)
            msg = msg1.decode('utf-8')
            while 1:
                if (msg == "E"):
                    print("Send Error")
                    s.close()
                    return 2
                elif (msg == "C"):
                    print("Success")
                    break
                else:
                    time.sleep(0.5)
                    msg1 = s.recv(1)
                    msg = msg1.decode('utf-8')
            s.close()
            return 0
        else:
            time.sleep(0.5)
            msg1 = s.recv(1)
            msg = msg1.decode('utf-8')
    #try:


    #except:
        #print("No server")
        #return 3
#标准文件发送函数(带检查，分段式检查文件，不带进度，适用于10m以上，1m每块）
def sendfile2(ip,port,head,whfile):
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    try:
        s.connect((ip, port))
        s.send(head.encode('utf-8'))
        time.sleep(0.5)
        msg1 = s.recv(1)
        msg = msg1.decode('utf-8')
        if(msg=="A"):
            print("Access denine")
            s.close()
            return 1
        elif(msg=="O"):
            file = open(whfile, 'rb')
            block=float(int(os.path.getsize(whfile))/1024)
            if(block%1!=0):
                block=int(block+1)
            i=1
            t=0
            while i<=block:
                s.send(str(file[t:t+1025]).encode('utf-8'))
                t+=1024
            time.sleep(0.5)
            msg1 = s.recv(1)
            msg = msg1.decode('utf-8')
            while 1:
                if(msg=="E"):
                    print("Send Error")
                    s.close()
                    return 2
                elif(msg=="C"):
                    print("Success")
                    break
                else:
                    time.sleep(0.5)
                    msg1 = s.recv(1)
                    msg = msg1.decode('utf-8')
            s.close()
            return 0
        else:
            time.sleep(0.5)
            msg1 = s.recv(1)
            msg = msg1.decode('utf-8')

    except:
        print("No server")
        return 0

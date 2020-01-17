#导入必要包
Version="0.0.1b"
import json
import socket,os,configparser
#import pymysql
#导入自定义函数

#内函数
curpath=os.path.dirname(os.path.realpath(__file__))
cfgpath=os.path.join(curpath,"Setting/sql.ini")  #读取到本机的配置文件
conf=configparser.ConfigParser()
print(cfgpath)
conf.read(cfgpath, encoding="utf-8")
sql_pw=conf.get("sql","pw")
sql_acc=conf.get("sql","acc")
sql_add=conf.get("sql","add")
version="0.0.1"




#建立连接
s = socket.socket()         # 创建 socket 对象
host = socket.gethostname() # 获取本地主机名
port = 19150             # 设置端口
s.bind((host, port))        # 绑定端口

s.listen(5)                 # 等待客户端连接
def login():
        print(addr)
        msg1 = c.recv(16)
        ac = msg1.decode('utf-8')
        print(ac)
        if ac == "ConnectTest":
            c.send(version.encode("utf-8"))
            c.close()
            return 0
        msg1 = c.recv(64)
        pd = msg1.decode('utf-8')
        print(pd)
        # 数据库校验
        #db = pymysql.connect(sql_add, sql_acc, sql_pw, "account")

        # 使用 cursor() 方法创建一个游标对象 cursor
        #cursor = db.cursor()
        #sql = "select*from acc where name='" + ac + "'"
        # print(sql)
        #cursor.execute(sql)

        # 使用 fetchone() 方法获取单条数据.
        #data = cursor.fetchall()
        # print(data)
        #if str(data) != "()":
            #for row in data:
                #if row[4] == pd:
                    #c.send("S".encode('utf-8'))
                    #c.close()
                #else:
                    #c.send("N".encode('utf-8'))
                    #c.close()
        c.send("S".encode('utf-8'))
        c.close()
        #else:
            #c.send("A".encode('utf-8'))
            #c.close()


while True:
    c, addr = s.accept()     # 建立客户端连接。
    login()


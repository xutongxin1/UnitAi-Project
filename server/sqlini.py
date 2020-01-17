import configparser
import os
#用os模块来读取
curpath=os.path.dirname(os.path.realpath(__file__))
cfgpath=os.path.join(curpath,"sql.ini")  #读取到本机的配置文件
conf=configparser.ConfigParser()
print(cfgpath)
conf.read(cfgpath, encoding="utf-8")
pw=conf.get("sql","pw")
acc=conf.get("sql","acc")
add=conf.get("sql","add")
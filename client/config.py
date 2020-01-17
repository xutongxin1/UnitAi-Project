import configparser,os,sys


curpath = os.path.dirname(os.path.realpath(__file__))
cfgpath = os.path.join(curpath, "config/user.ini")
cfgpath1 = os.path.join(curpath, "config/downloadobject.ini")
conf = configparser.ConfigParser()
conf1 = configparser.ConfigParser()
conf.read(cfgpath, encoding="utf-8")
conf1.read(cfgpath1, encoding="utf-8")

def config(a,b):
    return conf.get(a, b)

def downloadobjectconfig(a,b):
    return conf1.get(a, b)

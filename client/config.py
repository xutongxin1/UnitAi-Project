# -*- coding: utf-8 -*-

# 所有的客户端配置文件读写都应该通过该函数

import configparser, os, sys

curpath = os.path.dirname(os.path.realpath(__file__))
cfgpath = os.path.join(curpath, "config/user.ini")
cfgpath1 = os.path.join(curpath, "config/downloadobject.ini")
conf = configparser.ConfigParser()
conf1 = configparser.ConfigParser()
conf.read(cfgpath, encoding="utf-8")
conf1.read(cfgpath1, encoding="utf-8")


def config(file, topic, name):
    if file == "u" or file == "user":
        return conf.get(topic, name)
    elif file == "d":
        return conf1.get(topic, name)

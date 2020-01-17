#!/usr/bin/python
# -*- coding: utf-8 -*-
import requests,os
#下载地址
c = {'Name': 'Runoob'}
num=0 #从0开始存储
print("请输入图片前多个网址，#为结束，使用方法请看文档")
while 1:
    c[num]=input() #网址输入
    if c[num]=="#":
        print("一共输入了"+str(num)+"个网址")
        break
    num+=1
print("请输入保存位置，默认为本程序位置")
wh=input()
if wh!="":
    os.chdir(wh)
else :
    print("默认位置")
num1=0#网站计数
all=1#图片计数
while num1<num:
 a=c[num1]
 i = 1
 while True:
    try:
        if i < 10:
            Download_addres = a + "0" + str(i) + ".jpg"
        else:
            Download_addres = a + str(i) + ".jpg"
        f = requests.get(Download_addres)
        name = str(all) + ".jpg"
        # 下载文件
        b = f.content
        if b[0] == 60:
            print("完成第" + str(num1) + "个网站")
            break
        with open(name, "wb") as code:
            code.write(b)
        print(str(i) + "图片完成")
        # break
        all += 1
        i += 1
    except:
        print("没有网络或服务器错误")
        break
 num1+=1
print("程序完成")
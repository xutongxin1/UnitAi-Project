#!/usr/bin/python
# -*- coding: utf-8 -*-
import requests
#下载地址
c = {'Name': 'Runoob'}
num=0 #从0开始存储
while 1:
    c[num]=input() #网址输入
    if c[num]=="#":
        break
    num+=1

num1=0#网站计数
all=1#图片计数
while num1<num:
 a=c[num1]
 i = 1
 while True:
    if i<10:
         Download_addres=a+"0"+str(i)+".jpg"
    else:
        Download_addres=a+str(i)+".jpg"
    f=requests.get(Download_addres)
    name=str(all)+".jpg"
    #下载文件
    b=f.content
    if b[0]==60:
        print("Finish "+str(num)+" website")
        break
    with open(name,"wb") as code:
             code.write(b)
    print(str(i)+" is Ok")
    #break
    all+=1
    i+=1
 num1+=1
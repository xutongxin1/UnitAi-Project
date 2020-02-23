import bs4
import os
import sys
import urllib.request
  
path = './url.html' 
header = {
"accept": "image/webp,image/apng,image/*,*/*;q=0.8",
"accept-encoding": "gzip, deflate, br",
"accept-language": "zh-CN,zh;q=0.9",
"referer": "https://pixivic.com/popSearch",
"sec-fetch-mode": "no-cors",
"sec-fetch-site": "cross-site",
"user-agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/79.0.3945.130 Safari/537.36"
}

with open(path, 'rb') as fa:
    f = fa.readlines()
    #print(f)
    cou = 0
    for line in f:
        try:
            #print(line)
            res = (str(line)).find("href")
            cou+=1
            #rint(res)
            if res != -1:
                print(cou)
                url=line.decode('utf-8')
                print(url)
                url = url[res+4:res+90]
                print(url)
                request = urllib.request.Request(url, None, header)
                response = urllib.request.urlopen(request)
                print(response.headers['Content-Length'])
                with open("G:/img/"+str(cou)+".jpg", "wb") as f:
                    f.write(response.read())
                    f.close()
                print(response.geturl())
                print(response.info())# 返回报文头信息
        except:
            print("\n=========================")
            print("未经处理的异常在No.%d中"%cou)
            print("=========================\n")
            cou+=1
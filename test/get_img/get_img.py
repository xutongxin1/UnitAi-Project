import os
import sys
import urllib.request

# 设置消息头
url = "https://www.pixiv.net/artworks/77024666"
header = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; WOW64) \
        AppleWebKit/537.36 (KHTML, like Gecko) \
        Chrome/35.0.1916.114 Safari/537.36',
    'Cookie': 'AspxAutoDetectCookieSupport=1'
}
request = urllib.request.Request(url, None, header)
response = urllib.request.urlopen(request)
print(response.headers['Content-Length'])

with open("C:\\Users\\Jay\\Desktop\\img.jpg", "wb") as f:
    f.write(response.read())
print(response.geturl())
print(response.info())# 返回报文头信息
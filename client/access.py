import urllib, urllib.request, sys
import ssl

# client_id 为官网获取的AK， client_secret 为官网获取的SK
host = 'https://aip.baidubce.com/oauth/2.0/token?grant_type=client_credentials&client_id=UPCkp4V6fwqvS8kEyUIgGGBr&client_secret=x2YfRt4SsD4YplgAhyuGusubxNMj6GZY'
request = urllib.request.Request(host)
request.add_header('Content-Type', 'application/json; charset=UTF-8')
response = urllib.request.urlopen(request)
content = response.read()
if (content):
    print(content)
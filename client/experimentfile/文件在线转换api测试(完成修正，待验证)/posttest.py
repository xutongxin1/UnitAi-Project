import requests
import json
import base64
import os

apikey = "4fc3a688d6aaf8c4368bad7acf78c9e7"
if (True):
    input = "upload"
    outputformat = "pdf"
    headers = {'Content-Type': 'application/json'}
    urlbegin = "https://api.convertio.co/convert"
    data_begin = {
        "apikey": apikey,
        "input": "upload",
        "outputformat": outputformat,
        "filename": "123.doc"
    }

    req = requests.post(urlbegin, json.dumps(data_begin), headers=headers)
    result = json.loads(req.text)
    id = result['data']['id']
    print(id)
urlupload = "https://api.convertio.co/convert/" + id + "/123.doc"
file = open('123.doc', 'rb')
req = requests.put(urlupload, files=file)
result = json.loads(req.text)
print(result)
file.close()
print("begin!")
urlcheck = "https://api.convertio.co/convert/" + id + "/status"

while 1:
    req = requests.get(urlcheck, headers=headers)
    result1 = json.loads(req.text)
    try:
        if (result1['data']['step'] == "finish"):
            break
        else:
            print("Waiting")
            # print(result['data']['step_percent'])
    except:
        print(result1)

urlfinish = "https://api.convertio.co/convert/" + id + "/dl/base64"

req = requests.get(urlfinish, headers=headers)
result = json.loads(req.text)
try:
    base = result['data']['content']
    print(result)
except:
    print(result)

# print(base)
imgdata = base64.b64decode(base)
file = open('123.pdf', 'wb')
file.write(imgdata)
file.close()

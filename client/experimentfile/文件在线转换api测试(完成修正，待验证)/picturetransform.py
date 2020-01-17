import requests
import json
import base64
import os
apikey="4fc3a688d6aaf8c4368bad7acf78c9e7"
def picture(fr,to):
    input="url"
    file="http://google.com/"
    outputformat="png"
    headers = {'Content-Type': 'application/json'}
    urlupload = "https://api.convertio.co/convert"

    urlfinish="https://api.convertio.co/convert/:id/dl/:type"
    data_upload = {
            "apikey": apikey,
            "input":input,
            "file": file,
            "outputformat": outputformat,

              }

    req = requests.post(urlupload, json.dumps(data_upload), headers)
    result = json.loads(req.text)
    id=result['data']['id']
    print(id)
    print("begin!")
    urlcheck="https://api.convertio.co/convert/"+id+"/status"

    i=0
    while i==0:
        req = requests.get(urlcheck, headers)
        result = json.loads(req.text)
        if(result['data']['step']=="finish"):
            i=1
            print("end")
        else:
            print("Waiting")
            print(result['data']['step_percent'])


    urlfinish="https://api.convertio.co/convert/"+id+"/dl/"

    req = requests.get(urlfinish, headers)
    result = json.loads(req.text)
    base=result['data']['content']

    imgdata = base64.b64decode(base)
    file = open('1.jpg','wb')
    file.write(imgdata)
    file.close()

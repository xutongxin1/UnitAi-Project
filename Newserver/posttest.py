import json, requests

url = 'https://xutongxin.coding.net/api/v2/account/login'
data = {
    "account": "13360225383",
    "password":  "b2df1a9622be0bd3577153b0ccbd0877170a12ab"
}
headers = {
"Content-Type":"application/x-www-form-urlencoded"
}
req = requests.post(url, data=data, headers=headers)
# result = json.loads(req.text)
result = req.cookies.get_dict()

if "eid" in result.keys():
    print(result["eid"])

#with open("test.ppt", 'wb') as f:
    #f.write(req.content)

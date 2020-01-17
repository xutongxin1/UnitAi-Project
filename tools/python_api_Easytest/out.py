import json,requests
def test():
	url='http://localhost:5000/login'
	headers = {'Content-Type':'application/json'}
	data={
			"user": "xutongxin"
		}
	req = requests.post(url, json.dumps(data), headers)
	result = json.loads(req.text)

print(test)
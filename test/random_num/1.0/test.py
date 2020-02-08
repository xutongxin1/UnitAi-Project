import json
with open("data.json", 'r', encoding='utf-8') as f:
    print(f)
    dic = json.load(f)
    max = dic["max"]
    min = dic["min"]
    py = dic["py"]
print(max, min, py)
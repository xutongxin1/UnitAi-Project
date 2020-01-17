import hashlib
import json
acc=input()
pd=input()
sha256 = hashlib.sha256()
sha256.update(pd.encode('utf-8'))
res = sha256.hexdigest()
with open("./config/user.json",'r') as load_f:
  load_dict = json.load(load_f)
  print(load_dict)
#load_dict={}
load_dict.update({acc:res})
#print(load_dict)
with open("./config/user.json","w") as f:
   json.dump(load_dict,f)
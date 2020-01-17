import hashlib
path="C:/1.txt"
#md5=hashlib.md5(open(path, 'rb').read()).hexdigest()
f = open(path,'rb')
myHash = hashlib.md5()
while True:
    d = f.read(8096)
    if not d:
        break
    myHash.update(d)
md5 = myHash.hexdigest()
f.close()
print(md5)
import os

cmd_return = os.popen("path")
cmd_return = cmd_return.read()[5:-1]
#print(cmd_return)
#path = str(input("Python install path:"))
#cmd_return = cmd_return[:-1]

print(cmd_return)
print((os.popen('path')).read())
import os

cmd_return = os.popen("path")
cmd_return = cmd_return.read()[5:-1]#截掉开头的'PATH='
#print(cmd_return)
path = str(input("Python install path:"))

path_1 = path + ';'
path_2 = path + '\\Scripts;'
path_3 = path + '\\lib;'
path_4 = path + '\\lib\\site-packages;'
path_add = path_1 + path_2 + path_3 + path_4

# 用PyCharm运行的话，cmd_return结尾貌似会被加上一个句号"."
# 为什么要画蛇添足啊啊啊aaaaaa
if cmd_return[-1] == '.':#PyCharm
    cmd_return = cmd_return[:-1]
if cmd_return[-1] != '.':
    if cmd_return[-1] == ';':
        command = "setx /m path " + cmd_return + path_add
    elif cmd_return[-1] != ';':
        command = "setx /m path " + cmd_return + ";" + path_add

print(command)
#os.system(command)
os.system('pause')

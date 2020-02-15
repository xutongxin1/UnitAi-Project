import os, time
if(os.path.exists("_conda.exe")):
    path = os.getcwd()
    path_1 = path + ';'
    path_2 = path + '\\Scripts;'
    path_3 = path + '\\Library\\bin;'
    path_add = '"%Path%;' + path_1 + path_2 + path_3 + '" /m'
    command = "setx path " + path_add
    if os.system(command) == 0:
        os.system("color 2F")
        print("\n\n\n\n\n                  执行成功")
        time.sleep(5)
else:
    os.system("color 4F")
    print("\n\n\n\n\n           请将此文件放置在Miniconda目录下运行")
    time.sleep(5)
import os

search_files = []
for root, dirs, files in os.walk("D:\\"):
    for file in files:
        path = os.path.join(root, file)
        path = os.path.normcase(path)
        if file == "_conda.exe":
            search_files.append(path)
print(search_files)
path = str(search_files)[2:-14]
path = path.replace("\\\\", "\\")
path_1 = path + ';'
path_2 = path + '\\Scripts;'
path_3 = path + '\\Library\\bin;'
path_add = "%path%;" + path_1 + path_2 + path_3
command = "set path=" + path_add


print(command)
#os.system(command)

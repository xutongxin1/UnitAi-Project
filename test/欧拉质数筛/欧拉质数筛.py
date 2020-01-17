import time

time_start = time.time()
num_list = range(3,100000)
num_dict = {}
for x in num_list:
    if x%2 == 0:
        num_dict[x] = 'disable' #排除偶数
    else:
        num_dict[x] = 'endable'


check = 0
print(2)
for i in num_list:
    if num_dict[i] == 'endable':
        for j in range(3,i//2):
            if i%j == 0:
                check = 1
                break
        if check == 1:
            for n in range(1,1000//i):
                num_dict[i*n] = 'disable'
            check = 0
        else:
            print(i)

time_end = time.time()
time = time_end - time_start
print('time cost:%ds'%time)
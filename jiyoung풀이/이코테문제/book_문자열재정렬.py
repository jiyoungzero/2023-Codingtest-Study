# 구현

import sys # ord 쓰기!
input =sys.stdin.readline

command = input().rstrip()
num_arr = []
str_arr = []

for c in command:
    # if 65 <= ord(c) <= 90 or 97<= ord(c) <= 122: 
    
    ############ 한줄로 판별하기 ################
    if c.isalpha():
        str_arr.append(c)
    else:
        num_arr.append(int(c))
    str_arr.sort(key=lambda x:ord(x))
# print(*str_arr, sum(num_arr)) --> 코너 케이스 고려 안함!!

if sum(num_arr) != 0:
    str_arr.append(str(sum(num_arr)))
print(''.join(str_arr))
# 구현

import sys # ord 쓰기!
input =sys.stdin.readline

command = input().rstrip()
num_arr = []
str_arr = []

for c in command:
    if 65 <= ord(c) <= 90 or 97<= ord(c) <= 122:
        str_arr.append(c)
    else:
        num_arr.append(int(c))
    str_arr.sort(key=lambda x:ord(x))
print(*str_arr, sum(num_arr))
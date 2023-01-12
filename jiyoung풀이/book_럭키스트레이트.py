# 구현

import sys
input = sys.stdin.readline

n = int(input())
str_n = str(n)
length = len(str_n)
l_sum = 0
r_sum = 0
for i in range(length//2):
    l_sum += int(str_n[i])
for j in range(length//2, length):
    r_sum += int(str_n[j])
    
if l_sum == r_sum: print("LUCKY")
else: print("READY")

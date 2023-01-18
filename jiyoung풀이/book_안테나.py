# 정렬

import sys
input =sys.stdin.readline

# 일단 완탐은 
n = int(input())
arr = list(map(int, input().split()))
result = []

for i in range(1, max(arr)+1):
    tmp = 0
    for ele in arr:
        tmp += abs((i-ele))
    result.append((tmp,i))
result.sort()  
print(result[0][1])    
        
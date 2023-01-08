# greedy

import sys
input = sys.stdin.readline
from itertools import combinations

nums = [1,2,3,4]
combi = list(combinations(nums, 2))

n = int(input())
arr = list(map(int, input().split()))

arr.sort() # 오름차순

# 1 1 2 3 9 
result = 0
v = [False]*(1001)
v[0] =True 

for i in range(1,len(arr)):
    combi = list(combinations(arr, i))
    for ele in combi:
        v[sum(ele)] = True
    
for (i, value) in enumerate(v):
    if value == False:
        print(i)
        break

# 백트래킹

import sys
input = sys.stdin.readline
from itertools import combinations 

n = int(input())
arr = [list(map(int, input().split())) for _ in range(n)]

min_value = int(1e9)
nCr = list(combinations(range(1,n+1), n//2))

for i in range(len(nCr)//2):
    start = nCr[i]
    link = nCr[len(nCr)-i-1]
    tmp1, tmp2 = 0, 0
    
    for i in start:
        for j in start:
            tmp1 += arr[i-1][j-1]
            
    for i in link:
        for j in link:
            tmp2 += arr[i-1][j-1]
 
    
    min_value = min(min_value, abs(tmp1-tmp2))
    
    
print(min_value)
    
            


    
    


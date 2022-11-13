# 문제 스스로 풀어보기 

import sys
input = sys.stdin.readline
from itertools import combinations

def getComb(n,arr):
    comb_sum = []
    result = 0
    
    for i in range(1,n+1):
        for ele in combinations(arr,i):
            for i in ele:
                result += i
            comb_sum.append(result)
            result = 0
    return comb_sum



T = int(input())
for t in range(1,T+1):
    answer = 0
    
    n,k = tuple(map(int, input().split()))
    arr = list(map(int, input().split()))
    result = getComb(n, arr)
    
    answer = [ ele for ele in result if ele == k]
    
    
    print(f"#{t} {len(answer)}")
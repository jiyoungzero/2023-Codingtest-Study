# 백준 11497

import sys
import itertools
input = sys.stdin.readline

test_case = int(input())

# greedy? 오름차순으로 정렬하고 중간인덱스인 가장 큰 수를 기준으로 양 옆에 그 다름 수를 놓기
# 완탐?
for _ in range(test_case):
    n = int(input())
    arr = list(map(int, input().split()))
    
    result = []
    
    nPr = list(itertools.permutations(arr, n))
    for lst in nPr:
        tmp = -1
        for i in range(n):
            if i == (n-1):
                tmp = max(tmp, abs(lst[0]-lst[-1]))
            elif i < (n-1): 
                tmp = max(tmp, abs(lst[i]-lst[i+1]))
            
        result.append(tmp)
    print(min(result))
        
        
    

        
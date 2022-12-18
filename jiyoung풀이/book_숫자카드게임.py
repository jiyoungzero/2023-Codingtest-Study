# greedy 

# 문제 : 이코테 96페이지

import sys
input = sys.stdin.readline

n, m = map(int, input().split())
arr = [list(map(int, input().split())) for _ in range(n)]
result = []
for ele in arr:
    ele.sort()
    result.append(ele[0])
    
print(max(result))

# 백트래킹 

import sys
input = sys.stdin.readline 

n, m = map(int ,input().split())
result = []
 
 
def backtracking(start):
    if len(result) == m:
        print(" ".join(map(str, result)))
        return 
    for i in range(start, n+1):
        result.append(i)
        backtracking(i)
        result.pop()
backtracking(1)
        
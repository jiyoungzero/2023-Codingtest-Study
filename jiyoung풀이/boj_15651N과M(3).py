# 백트래킹, 재귀

import sys
input = sys.stdin.readline

n, m = map(int, input().split())
result = []

def backtracking():
    if len(result) == m:
        print(" ".join(map(str, result)))
        return 
    for i in range(1, n+1):
        result.append(i)
        backtracking()
        result.pop()
backtracking()
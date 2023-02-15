# 백트레킹 
import sys
input =sys.stdin.readline

n = int(input())
arr = [i for i in range(1,n+1)]
result = []
# 3 -> 1 2 3 /

def backtracking():
    if len(result) == n:
        print(*result)
        
    for i in range(1, n+1):
        if i not in result:
            result.append(i)
            backtracking()
            result.pop()
backtracking()
    

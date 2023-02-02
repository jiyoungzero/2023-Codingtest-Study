# 
import sys
input = sys.stdin.readline


n, m = map(int, input().split())
result = []
arr = [i for i in range(1,n+1)]

def backtracking():
    if len(result) == m:
        print(" ".join(map(str,result)))
        return
    for i in range(1,n+1):
        if (len(result) > 0 and (i > result[-1])) or (len(result) == 0):
            result.append(i)
            backtracking()
            result.pop() 
            
            
backtracking()
                
# print(result)

    
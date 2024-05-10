import sys
input = sys.stdin.readline 

n, m = map(int, input().split())
arr = list(map(int, input().split()))
answer = []

# 오름차순, 같은 수 가능, m개 고르기
def backtracking(sel, depth):
    global answer
    if len(sel) == m:
        print(sel)
        return 
    
    if depth == n:
        return 
    
    if len(sel) == 0:
        sel.append(arr[depth])
        backtracking(sel, depth+1)
        sel.pop()
    else:
        if sel[-1] <= arr[depth]:
            backtracking(sel+[arr[depth]], depth+1)
        
        backtracking(sel, depth+1)
backtracking([], 0)


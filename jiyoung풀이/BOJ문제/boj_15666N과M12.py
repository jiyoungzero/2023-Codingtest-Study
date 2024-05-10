import sys
input = sys.stdin.readline 

n, m = map(int, input().split())
arr = list(map(int, input().split()))
answer = []
arr.sort() # 1 7 9 9

# 오름차순, 같은 수 가능, m개 고르기
def backtracking(sel, depth):
    global answer
    if len(sel) == m:
        if sel not in answer:
            answer.append(sel)
        return
    
    if depth == n:
        return 
    
    for i in range(n):
        if len(sel) == 0 or sel[-1] <= arr[i]:
            backtracking(sel+[arr[i]], depth+1)
        backtracking(sel, depth+1)
backtracking([], 0)
answer.sort()
for ele in answer:
    print(*ele)


import sys
input = sys.stdin.readline 

n, m = map(int, input().split())
lst = list(map(int, input().split()))

answer = []
used = [False]*n
def backtracking(sel):
    global answer
    if len(sel) == m and sel not in answer:
        answer.append(sel)
        return 
        
    
    for i in range(n):
        if used[i]:continue
        used[i] = True
        backtracking(sel + [lst[i]])
        used[i] = False


backtracking([])
answer.sort()
for ele in answer:
    print(' '.join(map(str, ele)))
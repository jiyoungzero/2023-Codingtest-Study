import sys
input = sys.stdin.readline 

n, m = map(int, input().split())
lst = list(map(int, input().split()))

answer = set()
used = [False]*n
def backtracking(sel):
    global answer
    if len(sel) == m :
        answer.add(tuple(sel))
        return 
        
    
    for i in range(n):
        if used[i]:continue
        used[i] = True
        backtracking(sel + [lst[i]])
        used[i] = False


backtracking([])
for ele in sorted(list(answer)):
    print(' '.join(map(str, ele)))
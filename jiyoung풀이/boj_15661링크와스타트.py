# backtracking

import sys
input =sys.stdin.readline

n = int(input())
arr = [list(map(int, input().split())) for _ in range(n)]
visited = [0] * n
answer = int(1e9)

def get_min_answer():
    global answer
    start, link = 0,0
    for i in range(n):
        for j in range(n):
            if visited[i] and visited[j]:
                start += arr[i][j]
            elif not visited[i] and not visited[j]:
                link += arr[i][j]
    answer = min(answer, abs(start-link))
    return 


def backtracking(start, depth):
    global answer
    if depth == n//2:
        get_min_answer()
        return
    for i in range(start, n):
        if not visited[i]:
            visited[i] = True
            backtracking(i, depth+1)
            visited[i] = False
    
    
    
for i in range(0, n-1):
    backtracking(0, i)


print(answer)
    

    
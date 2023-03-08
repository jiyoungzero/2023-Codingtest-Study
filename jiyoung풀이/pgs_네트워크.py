# dfs/bfs

# 처음 내 풀이 
from collections import deque 

def solution(n, computers):
    answer = 0
    visited = [False]*n
    
    return n - bfs(0, visited, computers)


def bfs(start,visited, computers):
    que = deque(start)
    # visited[start] = True
    ans = 0
    while que:
        x = que.popleft()
        if not visited[x]:
            visited[x] = True
            for i in range(len(computers[x])):
                if i != x and computers[x][i]:
                    que.append(i)
                    ans += 1
    return ans
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

# bfs는 연결성, que가 끝나면 연결도 끝나는 것 (네트워크)
from collections import deque 


def solution(n, computers):
    answer = 0
    visited = [False for _ in range(n)]

    for connect in range(n):
        if not visited[connect]:
            bfs(n, connect, visited, computers)
            answer += 1

    return answer


def bfs(n, start,visited, computers):
    que = deque()
    visited[start] = True
    que.append(start)
    while que:
        x = que.popleft()
        visited[x] = True
        for i in range(n):
            if i != x and computers[x][i]:
                if not visited[i]:
                    que.append(i)
# 기본 개념 문제 dfs, bfs 
# dfs : 깊이, bfs : 너비 
from collections import deque
import sys
input = sys.stdin.readline

n, m, v = map(int, input().split())
graph = [[0]*(n+1) for _ in range(n+1)]

visited1 = [0] * (n+1)
visited2 = [0] * (n+1)

for _ in range(m):
    a, b = map(int, input().split())
    graph[a][b] = graph[b][a] = 1
    

# dfs : 재귀의 성질 
def dfs(v):
    visited1[v] = 1
    print(v, end=" ")
    for i in range(1, n+1):
        if visited1[i] == 0 and graph[v][i] == 1:
            dfs(i) # 재귀


# bfs : 큐의 성질 
def bfs(v):
    q = deque()
    q.append(v)
    visited2[v] = 1
    while q:
        v = q.popleft()
        print(v, end= " ")
        for i in range(1, n+1):
            if visited2[v] == 0 and graph[v][i] == 1:
                q.append(i)
                visited2[i] = 1
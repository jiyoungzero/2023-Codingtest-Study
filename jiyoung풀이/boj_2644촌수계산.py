# bfs

import sys
from collections import deque
input = sys.stdin.readline

n = int(input())
graph = [[] for _ in range(n+1)]
visited = [0]*(n+1)
a, b = map(int, input().split())
m = int(input())

for _ in range(m):
    x, y = map(int, input().split())
    graph[x].append(y)
    graph[y].append(x)
    
def bfs(start):
    que = deque()
    que.append(start)
    
    while que:
        v = que.popleft()
        for i in graph[v]:
            if visited[i] == 0:
                visited[i] = visited[v] + 1
                que.append(i)
                
bfs(a)                
print(visited[b] if visited[b] >0 else -1)
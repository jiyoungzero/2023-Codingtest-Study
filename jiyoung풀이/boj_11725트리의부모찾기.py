import sys
input =sys.stdin.readline
from collections import deque
n = int(input())
graph = [[] for i in range(n+1)]
for i in range(n-1):
    a, b = map(int, input().split())
    graph[a].append(b)
    graph[b].append(a)
    
parent=[0]*(n+1)    
que = deque()
que.append(1)
while que:
    now = que.popleft()
    for child in graph[now]:
        if parent[child] == 0:
            parent[child] = now
            que.append(child)
for p in parent[2:]:
    print(p)


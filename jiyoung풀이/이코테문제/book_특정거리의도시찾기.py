# dfs/bfs -> bfs

from collections import deque
import sys
input = sys.stdin.readline

n, m, k, x = map(int, input().split())
graph = [[] for _ in range(n+1)]
visited = [-1]*(n+1)
visited[x] = 0

for _ in range(m):
    a, b = map(int, input().split())
    graph[a].append(b) # 단방향이니까

def bfs(graph, start, visited):
    q = deque([start])
    while q:
        now = q.popleft()
        for i in graph[now]:
            if visited[i] == -1:
                visited[i] = visited[now] + 1
                q.append(i)
                
bfs(graph, x, visited)

flag = False

# print(visited)
for i in range(1, n+1):
    if visited[i] == k:
        print(i)
        flag = True
        
if not flag:
    print(-1)
    

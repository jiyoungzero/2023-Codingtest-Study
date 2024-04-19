import sys
input = sys.stdin.readline 
from collections import deque

n = int(input())
graph = [[] for _ in range(n+1)]
parent = [0]*(n+1)
for _ in range(n-1):
    a, b= map(int, input().split())
    graph[a].append(b)
    graph[b].append(a)
    
que = deque()
que.append(1)

def bfs():
    while que:
        cur = que.popleft()
        for leaf in graph[cur]:
            if parent[leaf] == 0:
                parent[leaf] = cur
                que.append(leaf)
                
bfs()
for ele in parent[2:]:
    print(ele)
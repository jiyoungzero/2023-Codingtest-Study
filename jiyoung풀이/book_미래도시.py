# 그래프 최단경로 (다익스트라)

import sys
input = sys.stdin.readline

n, m = map(int, input().split())
graph = [[0]*(n+1) for _ in range(n+1)]

for _ in range(m):
    a, b = map(int, input().split())
    graph[a][b] = graph[b][a] = 1
    
print(graph)
# 플로이드-워셜, 그래프탐색, bfs

import sys
input =sys.stdin.readline
INF = int(1e9)


n, m = map(int, input().split())
graph = [[INF]*(n+1) for _ in range(n+1)]
for _ in range(m):
    a, b = map(int, input().split())
    graph[a][b] = 1
    graph[b][a] = 1
    
# 자기 자신한테 가는 거 0
for i in range(n+1):
    graph[i][i] = 0
    
for k in range(1, n+1):
    for a in range(1, n+1):
        for b in range(1, n+1):
            graph[a][b] = min(graph[a][b], graph[a][k]+graph[k][b])

result = INF
result_idx = INF
for i in range(n, 0, -1):
    tmp = sum(graph[i][1:])
    result = min(result, tmp)
    if result == tmp:
        result_idx = i
print(result_idx)
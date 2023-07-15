# 그래프 최단경로 (다익스트라)

import sys
input = sys.stdin.readline
INF = int(1e9) # 무한 10억으로 설정

n, m = map(int, input().split())
graph = [[INF]*(n+1) for _ in range(n+1)]

# 자기 자신으로 가는 루트는 0으로
for a in range(1,n+1):
    for b in range(1,n+1):
        if a == b:
            graph[a][b] = 0
            
# 연결된 간선은 1로
for _ in range(m):
    a, b = map(int, input().split())
    graph[a][b] = graph[b][a] = 1

# k번 회사를 거쳐서 x에 최종 도착하는 최소 거리    
x, k = map(int, input().split())

# 플로이드 워셜 알고리즘 (dp와 비슷)
for i in range(1, n+1):
    for n in range(1, n+1):
        for m in range(1, n+1):
            graph[n][m] = min(graph[n][m], graph[n][i]+graph[i][m])
            
result = graph[1][k]+graph[k][x]

if result >= INF:
    print(-1)
else:
    print(result)
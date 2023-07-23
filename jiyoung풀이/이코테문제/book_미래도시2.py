# 플로이드 워셜 알고리즘 
# 모든 노드에 대해서 다른 모든 노드로 가는 최단 거리 정보를 구하는 알고리즘 


import sys
input = sys.stdin.readline
INF = int(1e9)

n, m = map(int, input().split())
graph = [[INF]*(n+1) for _ in range(n+1)]

for i in range(1,n+1): # 자기 자신에게 가는 거리는 0으로 초기화
    graph[i][i] = 0

for _ in range(m):
    a, b = map(int, input().split())
    graph[a][b] = 1
    graph[b][a] = 1
    
x, k = map(int, input().split())

# 플로이드 워셜 알고리즘 수행
for k in range(1, n+1):
    for a in range(1, n+1):
        for b in range(1, n+1):
            graph[a][b] = max(graph[a][b], graph[a][k]+graph[k][b])

# 문제의 핵심 (1번 노드에서 k까지의 최단 거리) + (k에서 x까지의 최단 거리)
distance = graph[1][k] + graph[k][x]

# 도달할 수 없다면 -1출력
print(distance if distance != INF else -1)



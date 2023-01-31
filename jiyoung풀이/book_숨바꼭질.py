# 최단 경로 n,m값이 크기 때문에 플로이드로는 안되고,,다익스트라로 풀기

import sys
input =sys.stdin.readline 
import heapq
INF = int(1e9)

n, m = map(int, input().split())
graph = [[] for _ in range(n+1)]

for _ in range(m):
    a, b = map(int, input().split())
    graph[a].append((b, 1)) # a에서 b로 가는 비용이 1
    graph[b].append((a, 1))

    
distance = [INF] * (n+1)
distance[0],distance[1] = 0,0
q = [(0, 1)] # 시작노드가 항상 1, 비용은 0으로 초기화
while q:
    dist, now = heapq.heappop(q)
    if dist > distance[now]:
        continue
    for i in graph[now]:
        cost = dist + i[1]
        if cost < distance[i[0]]:
            distance[i[0]] = cost
            heapq.heappush(q, (cost,i[0]))

result = max(distance)
print(distance.index(result), result, distance.count(result))     

            
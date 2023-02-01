# 그래프탐색

import sys
input = sys.stdin.readline
import heapq
INF = int(1e9)

n, k = map(int, input().split())
start = n
distance = [INF] * (100001)
graph = [ [] for i in range(100001)]

for i in range(1,100000): # 간선 정보 입력
    if 2*i<100001:
        graph[i].append((2*i,1))    
    graph[i].append((i+1,1))
    graph[i].append((i-1,1))

        
def dijkstra(start):
    q = []
    heapq.heappush(q, (0, start)) # 시작 노드일때는 시간 0으로 초기화
    distance[start] = 0
    while q:
        dist, now = heapq.heappop(q)
        if now == k:return distance
        if dist > distance[now]:
            continue
        for i in graph[now]:
            if i[1]+dist < distance[i[0]]:
                distance[i[0]] = i[1]+dist
                heapq.heappush(q, (i[1]+dist, i[0]))
     
dijkstra(start)
print(distance[k])

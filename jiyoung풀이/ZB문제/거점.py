import sys, heapq
from itertools import permutations
input = sys.stdin.readline
INF = int(1e9)


n, m = map(int, input().split())
graph = [[] for _ in range(n+1)]
for i in range(m):
    a, b, k = map(int, input().split())
    graph[a].append((b, k))
    graph[b].append((a, k))
    
x, y, z = map(int, input().split()) # 꼭 거쳐야 하는 노드 
dist_1 = dijk(1) # 1번 노드에서 출발했을 때의 최단 거리
dist_x = dijk(x) # x번 노드에서 출발했을 때의 최단 거리
dist_y = dijk(y) # y번 노드에서 출발했을 때의 최단 거리
dist_z = dijk(z) # z번 노드에서 출발했을 때의 최단 거리

route_1 = dist_1[x] + dist_x[y] + dist_y[z] + dist_z[n]
route_2 = dist_1[x] + dist_x[z] + dist_z[y] + dist_y[N]
route_3 = dist_1[y] + dist_y[x] + dist_x[z] + dist_z[N]
route_4 = dist_1[y] + dist_y[z] + dist_z[x] + dist_x[N]
route_5 = dist_1[z] + dist_z[x] + dist_x[y] + dist_y[N]
route_6 = dist_1[z] + dist_z[y] + dist_y[x] + dist_x[N]

answer = min(route_1, route_2, route_3, route_4, route_5, route_6)
if answer >= INF:  # 경로가 없는 경우
    answer = -1


    
def dijk(start):
    que = []
    distance = [INF]*(n+1)
    heapq.heappush(que, (0, start))
    distance[start] = 0
    while que:
        dist, now_x = heapq.heappop(que)
        if dist > distance[now_x]:
            continue
        
        for leaf in graph[now_x]: # leaf[0] = 다음 노드, leaf[1] = 다음 노드까지의 거리
            cost = leaf[1] + dist
            if cost < distance[leaf[0]]:
                distance[leaf[0]] = cost
                heapq.heappush(que, (cost, leaf[0]))
    return 
            
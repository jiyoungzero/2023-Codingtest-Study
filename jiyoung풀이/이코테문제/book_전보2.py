import sys
import heapq 
input = sys.stdin.readline

INF = int(1e9)

n, m, start = map(int, input.split()) # 도시의 개수, 통로의 개수, 메시지를 보내고자 하는 도시 c
graph = [[] for _ in range(n+1)]
distance = [INF]*(n+1)

for _ in range(m+1):
    x, y, z = map(int, input().split())
    graph[x].append((y, z))
    
def dijstra(start):
    q = []
    
    heapq.heappush(q, (0, start))
    while q:
        dist, now = heapq.heappop(q)
        if dist < distance[now]:continue
        
        for near in graph[now]:
            cost = near[1]+dist
            if cost < distance[near[0]]:
                distance[near[0]] = cost
                heapq.heappush(q, (cost, near[0]))

dijstra(start)

cnt = 0 #도달 가능한 도시
result = 0
for d in distance:
    if d != INF:
        cnt += 1
        result = max(result, d) # 한 노드(start)에서 다른 노드까지의 도달 가능한 것 중 가장 멀리 있는 노드의 최단 거리 
        
print(cnt-1, result) # 시작노드 제외(0이라고 해놨으므로)
        

                
        
    
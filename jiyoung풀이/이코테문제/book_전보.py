# 최단경로(그래프), 개선된 다익스트라(힙 자료구조 사용)

# 출발 도시에서 받을 수 있는 도시의 총 수
# 걸리는 시간 중의 최대값
import sys
import heapq
input = sys.stdin.readline
INF = int(1e9) # 무한 10억으로 설정

n, m , c = map(int, input().split()) # n: 도시의 개수, m : 통로의 개수, c: 메세지를 보내는 도시
graph = [[] for _ in range(n+1)]
distance = [INF] * (n+1)
start =c 
cnt = 0

for _ in range(m):
    x, y, z = map(int, input().split())
    # 도시 x에서 y로 가는 경로의 cost가 z
    graph[x].append((y, z))

def dij(start):
    q = []
    heapq.heappush(q, (0, start))
    distance[start] = 0
    
    while q:
        dist, now = heapq.heappop(q)
        if distance[start] < dist:
            continue
        for i in graph[now]:
            cost = dist + i[1]
            if cost < distance[i[0]]:
                distance[i[0]] = cost
                heapq.heappush(q,(cost, i[0]))
            
dij(c)
temp = 0
for d in distance:
    if d < INF:
        cnt += 1
        temp = max(temp, d)
print(cnt-1, end=" ") # 시작노드는 제외
print(temp)



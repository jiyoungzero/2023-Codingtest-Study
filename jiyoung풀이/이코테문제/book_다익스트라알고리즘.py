# 다익스트라 알고리즘 : 그래프에서 여러 개의 노드가 있을 때, 특정한 노드에서 출발하여 다른 노드로 가는 '각각의' 최단 경로를 구해주는 알고리즘 (단, 음의 경로는 없는 것으로 간주)

# 1. 출발 노드를 설정한다. 
# 2. 최단 거리 테이블을 초기화한다. (1차원 배열)
# 3. 방문하지 않은 노드 중에서 최단 거리가 가장 짧은 노드를 선택한다. 
# 4. 해당 노드를 거쳐 다른 노드로 가는 비용을 계산하여 최단 거리 테이블을 갱신한다. 
# 5. 위 과정에서  3, 4번을 반복한다. 


import heapq
import sys
input = sys.stdin.readline
INF = int(1e9)

n, m = map(int, input().split())
start = int(input())
graph = [[] for _ in range(n+1)] # 노드에 연결된 간선 정보 테이블
distance = [INF] * (n+1) # 최단 거리 테이블

# 간선 정보 입력받기
for i in range(n):
    a, b, c = map(int, input().split()) # a에서 b로 가는 비용이 c
    graph[a].append((b, c))
    

def dijkstra(start):
    q = []
    heapq.heappush(q, (0, start))
    distance[start] = 0
    
    while q:
        dist, now = heapq.heappop(q)
        if distance[now] < dist: # 이미 처리한 노드라면 무시
            continue
        
        for near in graph[now]:
            cost = dist + near[1]
            if cost < distance[near[0]]:
                distance[near[0]] = cost
                heapq.heappush(q, (cost, near[0]))

dijkstra(start)

# 모든 노드로 가기 위한 최단 거리 출력
for i in range(1, n+1):
    if distance[i] == INF:
        print("infinite")
    else:
        print(distance[i])
        
        
    
    
    





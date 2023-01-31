# 최단 경로 문제, n이 작아서 플로이드워셜로 풀어도 될 것 같다
import sys
input = sys.stdin.readline
import heapq
INF = int(1e9)

dxs, dys = [0,0,1,-1],[1,-1,0,0]
test_case = int(input())
for _ in range(test_case):
    n = int(input())
    graph = [list(map(int, input().split())) for _ in range(n)]
    
    distance = [[INF] * n for _ in range(n)]
    x, y = 0,0
    q = [(graph[x][y], x, y)]
    distance[x][y] = graph[x][y]
    
    while q:
        dist, x, y = heapq.heappop(q) # 가장 최단 거리가 짧은 노드의 거리, 현재 위치
        if distance[x][y] < dist:continue # 이미 처리한 노드면 통과과
        
        for k in range(4):
            nx, ny = x+dxs[k], y + dys[k]
            if 0<=nx<n and 0<=ny<n:
                cost = dist + graph[nx][ny]
                if cost < distance[nx][ny]:
                    distance[nx][ny] = cost
                    heapq.heappush(q,(distance[nx][ny], nx, ny))
    
    print(distance[n-1][n-1])
        


    
    
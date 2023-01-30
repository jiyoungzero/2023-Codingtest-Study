# 플로이드 워셜, 최단 경로 알고리즘 

# 이중배열을 이용하여 삼중반복문으로 구현 / 모든 노드에서 다른 모든 지점까지의 최단 경로를 계산 (당연히 다익스트라로도 커버가능)

import sys
input = sys.stdin.readline

n = int(input()) # 도시의 개수
m = int(input()) # 간선의 개수
graph = [ [int(1e9)]*(n+1) for _ in range(n+1)]
for _ in range(m):
    a, b, c = map(int, input().split())
    graph[a][b] = c
    
# 자기에서 자신으로 가는 경로는 0으로 초기화
for a in range(1, n+1):
    for b in range(1, n+1):
        if a == b:
            graph[a][b] = 0
    
for k in range(1, n+1):
    for a in range(1, n+1):
        for b in range(1, n+1):
            graph[a][b] = min(graph[a][b], graph[a][k] + graph[k][b])
            
for i in range(1,n+1):
    for j in range(1, n+1):
        if graph[i][j] == int(1e9):
            print("0", end=" ")
        else:print(graph[i][j], end=" ")
    print()

            



# 최단 경로 그래프

import sys
input = sys.stdin.readline

n, m = map(int ,input().split())
graph = [[int(1e9)]*(n+1) for _ in range(n+1)]
result = 0

for _ in range(m):
    a, b = map(int ,input().split())
    # 성적 : a < b
    graph[a][b] = 1 # a<b
    # graph[b][a] = 1 #  b>a
    
for a in range(1, n+1):
    for b in range(1, n+1):
        if a == b:graph[a][b] = 0 # 같은 사람이면 0으로 초기화
        
# 모두 연결된 경우를 cnt += 1
for k in range(1, n+1):
    for a in range(1, n+1):
        for b in range(1, n+1):
            graph[a][b] = min(graph[a][b], graph[a][k]+graph[k][b])
            
# 최단거리를 구했다면 연결됐다는 거니까...
for a in range(1, n+1):
    flag = True
    for b in range(1, n+1):
        # 둘 다 몰라야지, 왜냐면 한 쪽이라도 알면 순서는 정해지니께
        if graph[a][b] == int(1e9) and graph[b][a] == int(1e9):
            flag = False
    if flag:result+=1
print(result)
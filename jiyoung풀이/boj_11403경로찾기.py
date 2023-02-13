# 그래프 탐색
import sys
input =sys.stdin.readline
INF = int(1e9)
n = int(input())
graph = []

for _ in range(n):
    tmp = list(map(int, input().split()))
    append_list = []
    for ele in tmp:
        if ele == 0:
            append_list.append(INF)
        else:
            append_list.append(ele)
    graph.append(append_list)

    
# # 0인 부분 INF로 만들고 자기 자신 한테 가는 거는 0
# for i in range(n):
#     for j in range(n):
#         if i==j:
#             graph[i][j] = INF
        
for k in range(n):
    for a in range(n):
        for b in range(n):
            graph[a][b] = min(graph[a][b], graph[a][k] + graph[k][b])

for i in range(n):
    for j in range(n):
        if graph[i][j] < INF:
            print(1, end=" ")
        else:
            print(0, end=" ")
    print()
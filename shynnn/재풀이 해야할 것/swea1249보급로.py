# D2
# 우선 완탐(dfs)으로는 풀 수 있고..
# 상하좌우로만 가능
# python 3초

# [N-1][N-1] 도착 시 return
# 백트래킹

# T = int(input())
# for t in range(1, T+1):
# import sys
# sys.setrecursionlimit(10**6)

# N = int(input())
# load = [list(map(int, input())) for _ in range(N)]
# visited = [[0] * N for _ in range(N)]
# dp = [[10] * N for _ in range(N)]
# result = 100000

# dx, dy = [0, -1, 0, 1], [1, 0, 1, 0]


# def dfs(x, y):
#     global result
#     global load
#     if x == N-1 and y == N-1:
#         result = min(result, dp[N-1][N-1])
#         return
#     if dp[x][y] >= result:
#         return

#     for i in range(4):
#         xx, yy = dx[i]+x, dy[y]+y
#         if xx < 0 or xx >= N or yy < 0 or yy >= N:
#             continue
#         if (visited[xx][yy] == 0 or (dp[xx][yy] > dp[x][y]+load[xx][yy])):
#             print("여기")
#             dp[xx][yy] = dp[x][y] + load[xx][yy]
#             visited[xx][yy] = 1
#             dfs(xx, yy)


# visited[0][0] = 1
# dfs(0, 0)
# print(dp)
# print(result)

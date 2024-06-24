# Lv. 3
from itertools import product
import sys
input = sys.stdin.readline 


# 1) 내 풀이
# n, m = map(int, input().split())
# arr = [list(map(int, input().split())) for _ in range(n)]
# friends = [tuple(map(int, input().split())) for _ in range(m)]
# result = 0


# def in_range(x, y):
#     return 0 <= x < n and 0 <= y < n

# def get_result(paths):
#     tmp = 0
#     visited = [[False]*n for _ in range(n)]
#     dxs, dys = [0,0,1,-1],[1,-1,0,0] # 아래, 위, 오른쪽, 왼쪽

    
#     for i, friend in enumerate(friends):
#         x, y = friend
#         x -= 1
#         y -= 1
#         tmp += arr[x][y]
#         visited[x][y] = True
        
#         for path in paths:
#             # print(paths, path)
#             k = path[i]
#             nx, ny = x + dxs[k], y + dys[k]
#             if not in_range(nx,ny): return -1 # 격자 밖 -> 최대의 경우가 될 수 없음
#             if not visited[nx][ny]:
#                 visited[nx][ny] = True
#                 tmp += arr[nx][ny]
#             x, y = nx, ny
        
#     return tmp


# # [0초일때 m명의 경로], [1초일때], [2초일때], [3초일때] 
# def get_path(path): # path = [[0,0,1,2],[0,0,2,3],[2,3,1,0]]
#     global result, possible_path
    
#     p_len = len(possible_path)
#     # 0~3까지 선택 
#     if len(path) == 3:
#         result = max(result, get_result(path))
#         return 
    
#     for i in range(p_len):
#         path.append(possible_path[i])
#         get_path(path)
#         path.pop()



# possible_path = list(product(list(range(4)), repeat = m))
# get_path([])
# print(result)

# 2) 다른 풀이 -> 백트래킹에서 결과값을 얻어오고 싶을 때, 파라미터 + 외부 변수값으로 세팅하면 됨
from sys import stdin
from itertools import product

dx = [0, 0, -1, 1]
dy = [-1, 1, 0, 0]

def dfs(path, x, y, routes):
    if len(path) == 4:
        routes.append(path[:])
        return
    for i in range(4):
        nx, ny = x + dx[i], y + dy[i]
        if 0 <= nx < N and 0 <= ny < N and (nx, ny) not in path:
            path.append((nx, ny))
            dfs(path, nx, ny, routes)
            path.pop()

def get_total_fruits(routes):
    result = 0
    visited = set()
    for route in routes:
        for x, y in route:
            if (x, y) in visited:
                return 0  # 경로가 겹치는 경우 과일을 수집하지 않음
            visited.add((x, y))
            result += board[x][y]
    return result

# 입력 받기
N, M = map(int, stdin.readline().split())
board = [list(map(int, stdin.readline().strip().split())) for _ in range(N)]
friend_points = []
for _ in range(M):
    a, b = map(int, stdin.readline().split())
    friend_points.append([a - 1, b - 1])

# 각 친구의 가능한 모든 경로 찾기
friends_routes = []
for i in range(M):
    routes = []
    dfs([friend_points[i]], friend_points[i][0], friend_points[i][1], routes)
    friends_routes.append(routes)

# 가능한 모든 경로 조합을 통해 최대 과일 수 찾기
res = 0
for comb in product(*friends_routes):
    res = max(res, get_total_fruits(comb))

print(res)
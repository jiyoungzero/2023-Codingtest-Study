# Lv. 3
from itertools import product
import sys
input = sys.stdin.readline 



n, m = map(int, input().split())
arr = [list(map(int, input().split())) for _ in range(n)]
friends = [tuple(map(int, input().split())) for _ in range(m)]
result = 0


def in_range(x, y):
    return 0 <= x < n and 0 <= y < n

def get_result(paths):
    tmp = 0
    visited = [[False]*n for _ in range(n)]
    dxs, dys = [0,0,1,-1],[1,-1,0,0] # 아래, 위, 오른쪽, 왼쪽

    
    for i, friend in enumerate(friends):
        x, y = friend
        x -= 1
        y -= 1
        tmp += arr[x][y]
        visited[x][y] = True
        
        for path in paths:
            # print(paths, path)
            k = path[i]
            nx, ny = x + dxs[k], y + dys[k]
            if not in_range(nx,ny): return -1 # 격자 밖 -> 최대의 경우가 될 수 없음
            if not visited[nx][ny]:
                visited[nx][ny] = True
                tmp += arr[nx][ny]
            x, y = nx, ny
        
    return tmp


# [0초일때 m명의 경로], [1초일때], [2초일때], [3초일때] 
def get_path(path): # path = [[0,0,1,2],[0,0,2,3],[2,3,1,0]]
    global result, possible_path
    
    p_len = len(possible_path)
    # 0~3까지 선택 
    if len(path) == 3:
        result = max(result, get_result(path))
        return 
    
    for i in range(p_len):
        path.append(possible_path[i])
        get_path(path)
        path.pop()



possible_path = list(product(list(range(4)), repeat = m))
get_path([])
print(result)

    
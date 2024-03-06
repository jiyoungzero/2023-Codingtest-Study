from collections import deque
import copy

n, m = map(int, input().split())
arr = [list(map(int, input().split())) for _ in range(n)]
answer = 0
def in_range(x, y):
    return 0 <= x < n and 0 <= y < n

def bfs(x, y, color):
    que = deque()
    que.append((x, y))
    dxs, dys = [0,0,1,-1],[1,-1,0,0]
    group_size, rainbow_cnt = 1, 0
    group_info, rainbows = [[x, y]], []
    
    while que:
        x, y = que.popleft()
        for d in range(4):
            nx, ny = x + dxs[d], y + dys[d]
            if not in_range(nx, ny):continue
            if not visited[nx][ny]:
                if arr[nx][ny] == color:
                    visited[nx][ny] = 1
                    que.append((nx,ny))
                    group_info.append((nx, ny))
                    group_size += 1
                if arr[nx][ny] == 0:
                    visited[nx][ny] = 1
                    que.append((nx,ny))
                    group_size += 1
                    rainbow_cnt += 1
                    rainbows.append((nx,ny))
    # 무지개블록은 방문 다시 해제
    for x, y in rainbows:
        visited[x][y] = 0
    return [group_size, rainbow_cnt, group_info+rainbows]

def remove(group):
    global arr
    for x, y in group:
        arr[x][y] = -2

def gravity():
    global arr
    nxt_arr = [[-2]*n for _ in range(n)]
    for j in range(n):
        row = n-1
        for i in range(n-1, -1, -1):
            if arr[i][j] == -2:continue
            elif arr[i][j] == -1:
                row = i
                nxt_arr[row][j] = arr[i][j]
                row -= 1
            else:
                nxt_arr[row][j] = arr[i][j]
                row -= 1
                
    arr = copy.deepcopy(nxt_arr)
    return 

def rotate():
    global arr
    rotate_arr = list(map(list, zip(*arr)))[::-1]
    arr = copy.deepcopy(rotate_arr)
    return 

while True:
    visited = [[0]*n for _ in range(n)]
    possible_groups = []
    for i in range(n):
        for j in range(n):
            if arr[i][j] > 0 and not visited[i][j]:
                visited[i][j] = 1
                group = bfs(i, j, arr[i][j]) # 블록 크기, 무지개 개수, 기준좌표
                if group[0] > 1:
                    possible_groups.append(group)
    possible_groups.sort(reverse=True)     
    
    if not possible_groups:break
    
    remove(possible_groups[0][2])
    answer += possible_groups[0][0]**2
    
    gravity()
    rotate()
    gravity()
    
print(answer)
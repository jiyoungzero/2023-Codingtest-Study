import sys
input = sys.stdin.readline 
from collections import deque
import copy

n, q = map(int, input().split())
arr = [list(map(int, input().split())) for _ in range(2**n)]
cmds = list(map(int, input().split()))
visited = [[False]*(2**n) for _ in range(2**n)]
dxs, dys = [0,0,1,-1],[1,-1,0,0]

def in_range(x, y):
    return 0 <= x < 2**n and 0 <= y < 2**n

def rotate_glaciers(level):
    global arr
    side = 2**level
    nxt_arr = copy.deepcopy(arr)

    for i in range(0, 2**n, side):
        for j in range(0, 2**n, side):
            # 4 부분으로 자르기
            inner_side = side//2
            
            up_left = [i, j, i+inner_side, j+inner_side]
            down_left = [i+inner_side, j, i+side, j+inner_side]
            up_right = [i, j+inner_side, i+inner_side, j+side]
            down_right = [i+inner_side, j+inner_side, i+side, j+side]
            # 1) 좌측 아래 -> 좌측 위
            for ii in range(down_left[0], down_left[2]):
                for jj in range(down_left[1], down_left[3]):
                    nxt_arr[ii-inner_side][jj] = arr[ii][jj] 
            # 2) 우측 아래 -> 좌측 아래
            for ii in range(down_right[0], down_right[2]):
                for jj in range(down_right[1], down_right[3]):
                    nxt_arr[ii][jj-inner_side] = arr[ii][jj]

            # 3) 우측 위 -> 우측 아래
            for ii in range(up_right[0], up_right[2]):
                for jj in range(up_right[1], up_right[3]):
                    # print((ii, jj), "->", (ii+2, jj))
                    nxt_arr[ii+inner_side][jj] = arr[ii][jj]

            # 4) 좌측 위 -> 우측 위
            for ii in range(up_left[0], up_left[2]):
                for jj in range(up_left[1], up_left[3]):
                    nxt_arr[ii][jj+inner_side] = arr[ii][jj]
    arr = copy.deepcopy(nxt_arr)


def melting():
    global arr
    new_arr = copy.deepcopy(arr)

    for i in range(2**n):
        for j in range(2**n):
            if arr[i][j] > 0:
                ice_cnt = 0
                for dir in range(4):
                    ni, nj = i + dxs[dir], j + dys[dir]
                    if in_range(ni, nj) and arr[ni][nj] > 0:
                        ice_cnt += 1
                if ice_cnt < 3:
                    new_arr[i][j] = arr[i][j] - 1
    # 동시에 얼음이 녹음 -> 업데이트
    arr = copy.deepcopy(new_arr)


def get_all_glaciers():
    result = 0
    for i in range(2**n):
        for j in range(2**n):
            result += arr[i][j]
    print(result)

def bfs(sx, sy):
    global visited
    result = 1

    que = deque()
    que.append((sx, sy))
    visited[sx][sy] = True
    while que: 
        x, y = que.popleft()
        for dir in range(4):
            nx, ny = x + dxs[dir], y + dys[dir]
            if not in_range(nx, ny):continue
            if not visited[nx][ny] and arr[nx][ny] > 0:
                que.append((nx, ny))
                result += 1
                visited[nx][ny] = True
    return result

def get_largest_glacier():
    global visited
    largest = 0
    for i in range(2**n):
        for j in range(2**n):
            if not visited[i][j] and arr[i][j] > 0:
                largest = max(largest, bfs(i, j))
    print(largest)

for level in cmds:
    rotate_glaciers(level)
    melting()


get_all_glaciers()

get_largest_glacier()


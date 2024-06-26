import sys
input = sys.stdin.readline 
from collections import deque
import copy

K, M = map(int, input().split())
arr = [list(map(int, input().split())) for _ in range(5)]
fragments = deque(list(map(int, input().split())))
answer = 0
dxs, dys = [0,0,1,-1],[1,-1,0,0]

def in_range(x, y):
    return 0 <= x < 5 and 0 <= y < 5

def fake_rotate_90(sx, sy, matrix): # 1차 획득가치를 위한 회전
    c_arr = copy.deepcopy(matrix)
    for x in range(sx, sx + 3):
        for y in range(sy, sy+3):
            ox, oy = x - sx, y - sy
            rx, ry = oy, 3 - ox - 1
            c_arr[rx+sx][ry+sy] = matrix[x][y]
    return c_arr

def real_rotate_90(sx, sy):
    global arr
    r_arr = copy.deepcopy(arr)
 
    for x in range(sx, sx + 3):
        for y in range(sy, sy+3):
            ox, oy = x - sx, y - sy
            rx, ry = oy, 3 - ox - 1
            r_arr[rx+sx][ry+sy] = arr[x][y]

    arr = copy.deepcopy(r_arr)
    return

def find_largest():
    lst = [] # (유물가치, 회전각도, y, x)
    for i in range(3):
        for j in range(3): 
            x, y = i + 1, j + 1 # 회전중심x, 회전중심y

            # 90도 회전한 결과
            c_arr1 = fake_rotate_90(i,j,arr)

            tmp1 = bfs(c_arr1)
            tmp1_value = len(tmp1)
            if len(tmp1) > 0:lst.append((tmp1_value, 1, y, x))
            
            # 180도 회전한 결과
            c_arr2 = fake_rotate_90(i, j, c_arr1)
 
            tmp2 = bfs(c_arr2)
            tmp2_value = len(tmp2)
            if len(tmp2) > 0:lst.append((tmp2_value, 2, y, x))

            # 270도 회전한 결과 
            c_arr3 = fake_rotate_90(i, j, c_arr2)
            tmp3 = bfs(c_arr3)
            tmp3_value = len(tmp3)
            if len(tmp3) > 0: lst.append((tmp3_value, 3, y, x))

    if len(lst) > 0:
        lst.sort(key = lambda x:(-x[0], x[1], x[2], x[3]))
        final_rotate = lst[0]
        r_cnt, x, y = final_rotate[1], final_rotate[3], final_rotate[2]
        for _ in range(r_cnt):
            real_rotate_90(x-1, y-1)  
    else:
        return -1

def bfs(matrix): # 3개 이상 연결된 유물의 위치를 리턴 (행, 열)
    values = []
    
    for j in range(5): # 열이 작은 순으로 
        for i in range(4, -1, -1): # 행이 큰 순으로 
            if (i, j) in values:continue

            que = deque()
            visited = [[False]*5 for _ in range(5)]
            que.append((i,j))
            visited[i][j] = True
            pos = [(i, j)]
            
            while que:
                x, y = que.popleft()
                for dir in range(4):
                    nx, ny = x + dxs[dir], y + dys[dir]
                    if not in_range(nx, ny):continue
                    if not visited[nx][ny] and matrix[i][j] == matrix[nx][ny]:
                        pos.append((nx,ny))
                        que.append((nx,ny))
                        visited[nx][ny] = True
            if len(pos) >= 3:
                values += pos
    return values # 행, 열


def delete_fill_places(targets):
    global arr, fragments
    result = len(targets)
    targets.sort(key=lambda x:(x[1], -x[0]))

    for target in targets:
        x, y = target
        arr[x][y] = fragments.popleft()
    return result

def process(): # 유물 획득과정
    result = 0
    while True:
        targets = bfs(arr)
        if len(targets) == 0:
            break
        result += delete_fill_places(targets)
    return result


for _ in range(K):
    if find_largest() == -1:
        break
    answer = process()
    if answer > 0:
        print(answer, end = " ")
    else:
        break

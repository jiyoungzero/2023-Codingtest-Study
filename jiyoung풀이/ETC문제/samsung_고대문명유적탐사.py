import sys
input = sys.stdin.readline 
from collections import deque
import copy

# K = 탐사 반복 횟수
# M = 유물 조각의 개수 -> fragments
K, M = map(int, input().split())
arr = [list(map(int, input().split())) for _ in range(5)]
fragments = deque(list(map(int, input().split())))
# fragments = deque()
answer = 0
dxs, dys = [0,0,1,-1],[1,-1,0,0]

def in_range(x, y):
    return 0 <= x < 5 and 0 <= y < 5

def fake_rotate_90(sx, sy): # 1차 획득가치를 위한 회전
    c_arr = copy.deepcopy(arr)
    for x in range(sx, sx + 3):
        for y in range(sy, sy+3):
            ox, oy = x - sx, y - sy
            rx, ry = oy, 3 - ox - 1
            c_arr[rx+sx][ry+sy] = arr[x][y]
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
            for r_cnt in range(3):
                c_arr = fake_rotate_90(i, j)
                tmp = bfs(c_arr)
                tmp_value = 0 # 유적의 가치
                for row in tmp:
                    tmp_value += len(row)

                if len(tmp) > 0:
                    lst.append((tmp_value, r_cnt, y, x))
    if len(lst) > 0:
        lst.sort(key = lambda x:(-x[0], x[1], x[2], x[3]))
        final_rotate = lst[0]
        r_cnt, x, y = final_rotate[1], final_rotate[3], final_rotate[2]
        for _ in range(r_cnt+1):
            real_rotate_90(x-1, y-1)  
    else:
        return -1

def bfs(matrix): # 3개 이상 연결된 유물의 위치를 리턴 (행, 열)
    values = []
    checked = []
    
    for j in range(5): # 열이 작은 순으로 
        for i in range(4, -1, -1): # 행이 큰 순으로 
            if (i, j) in checked:continue

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
                checked += pos
                values.append(pos)
    return values # 행, 열

def delete_fill_places(targets):
    global arr, fragments
    result = 0

    
    for target in targets:
        target.sort(key = lambda x:(x[1],-x[0]))
        result += len(target)

        for x, y in target:
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




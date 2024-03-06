import copy
from collections import deque

BLACK = -1
RAINBOW = 0
BLANK = -2

n, m = map(int, input().split())
arr = [list(map(int, input().split())) for _ in range(n)]
dxs, dys = [0,0,1,-1], [1,-1,0,0]
answer = 0
# 그룹 : 일반 블록 하나 이상 + 해당 일반 블록의 숫자가 모두 같아야 함. + 검은색 안됨 
# 기준 블록 : 무지개 블록을 제외하고 행의 번호 작기, 열의 번호가 작은 블록

# find_largest_group : 무지개 많은 순, 기준블록의 행이 큰 순, 열이 큰 순
# 위에서 찾은 하나의 큰 그룹에 속한 블록을 제거
# answer += (위에서 찾은 그룹의 수)**2
# 중력에 의해 arr가 밑으로 떨어짐
# 90도 반시계방향으로 회전
# 다시 중력
def in_range(x, y):
    return 0 <= x < n and 0 <= y < n


def gravity():
    global arr
    nxt_arr = [[BLANK]*n for _ in range(n)]
    
    for j in range(n):
        tmp = n-1
        for i in range(n-1, -1, -1):
            if arr[i][j] == BLANK:continue
            elif arr[i][j] == BLACK:
                tmp = i
                nxt_arr[tmp][j] = arr[i][j]
                tmp -= 1
                
            elif arr[i][j] != BLANK: 
                nxt_arr[tmp][j] = arr[i][j]
                tmp -= 1
    
    arr = copy.deepcopy(nxt_arr)
    return 

def get_center(group_lst):
    group_lst.sort(key = lambda x : (x[0], x[1]))
    for x, y in group_lst:
        if arr[x][y] != RAINBOW:
            return (x, y)


def is_group(group_lst):
    normal =0
    for x, y in group_lst:
        if arr[x][y] > RAINBOW:
            normal += 1
    if len(group_lst) > 1 and normal > 0:
        return True
    else: return False

def find_group(sx, sy):
    rainbow_cnt = 0
    center_x, center_y = 0, 0
    que = deque()
    que.append((sx, sy))
    visited[sx][sy] = True
    
    group_lst = [(sx, sy)]
    num = arr[sx][sy]
    while que:
        x, y = que.popleft()
        for k in range(4):
            nx, ny = x + dxs[k], y + dys[k]
            if not in_range(nx, ny):
                continue
            if not visited[nx][ny] and arr[nx][ny] != BLACK:
                if arr[nx][ny] == num or arr[nx][ny] == RAINBOW:
                    if arr[nx][ny] == RAINBOW:
                        rainbow_cnt += 1
                    group_lst.append((nx, ny))
                    visited[nx][ny] = True
                    que.append((nx, ny))
                    
                    
    if is_group(group_lst):
        center_x, center_y = get_center(group_lst)
        return (rainbow_cnt, center_x, center_y)
    else:
        for x, y in group_lst:
            visited[x][y] = False
            return []


def find_largest_group():
    lst = []
    has_group = False
    for i in range(n):
        for j in range(n):
            if arr[i][j] != BLANK and not visited[i][j]:
                result = find_group(i,j) # 무지개블록 개수, 기준 블록의 행/열
                if len(result) > 0:
                    has_group = True
                    lst.append(result)
    if has_group:
        lst.sort(key = lambda x : (-x[0], -x[1], -x[2]))
        return [lst[0][1], lst[0][2]]
    else:
        return False

def remove_group(sx, sy):
    global arr, answer
    # x, y기준으로 그룹인 곳들 다 -2으로 만들기(blank)
    group_lst = [(sx, sy)]
    que = deque()
    visited2 = [[False]*n for _ in range(n)]
    que.append((sx, sy))
    visited2[sx][sy] = True
    
    num = arr[sx][sy]
    while que:
        x, y = que.popleft()
        for k in range(4):
            nx, ny = x + dxs[k], y + dys[k]
            if not in_range(nx, ny):
                continue
            if not visited2[nx][ny] and arr[nx][ny] != BLACK:
                if arr[nx][ny] == num or arr[nx][ny] == RAINBOW:
                    group_lst.append((nx, ny))
                    visited2[nx][ny] = True
                    que.append((nx, ny))
    plus = 0
    for x, y in group_lst:
        arr[x][y] = BLANK
        plus += 1
    
    answer += (plus)**2
    return

def rotate_90(): # 반시계
    global arr
    rotate_arr = list(map(list, zip(*arr)))[::-1]
    arr = copy.deepcopy(rotate_arr)
    return 

while True:
    visited = [[False]*n for _ in range(n)]
    flag = find_largest_group()
    if flag == False:
        break
    else:
        remove_group(flag[0], flag[1])      
        gravity()
        rotate_90()
        gravity()
        print()
        for row in arr:
            print(*row)  


print(answer)
        
    
    
    


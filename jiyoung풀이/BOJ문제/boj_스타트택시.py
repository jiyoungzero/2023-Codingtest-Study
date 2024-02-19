# 구현

import sys
input = sys.stdin.readline
from collections import deque

# 승객 : 거리 짧을 수록, 행번호가 작은, 열 번호가 작은
# 충전 연료 : 소모한 연료(거리) * 2
# 중간에 연료가 떨어지면 or 모든 손님 이동 불가 시 -1(목적지 도착 외)

BLANK = 0
WALL = 1

n, m, now_fuel = map(int, input().split())
grid = [list(map(int, input().split())) for _ in range(n)]
taxi_x, taxi_y = map(int, input().split())
taxi_x -= 1
taxi_y -= 1

dxs, dys = [0,0,1,-1],[1,-1,0,0]
for i in range(2, m+2):
    a, b, c, d = map(int, input().split())
    grid[a-1][b-1] = (i, 'start')
    grid[c-1][d-1] = (i, 'end')
    
def in_range(x, y):
    return 0 <= x < n and 0 <= y < n
    
def find_shortest_pos(): # 현재 택시위치에서 가장 가까운 손님
    que = deque()
    visited = [[-1]*n for _ in range(n)]
    que.append((taxi_x, taxi_y))
    visited[taxi_x][taxi_y] = 0
    
    result = [] # (택시와의 거리, 손님 인덱스, x, y)
    # 현재 택시 위치가 출발지일 경우
    if type(grid[taxi_x][taxi_y]) != int and grid[taxi_x][taxi_y][1] == 'start':
        result.append((0, grid[taxi_x][taxi_y][0], taxi_x, taxi_y))
    while que:
        x, y = que.popleft()
        for k in range(4):
            nx, ny = x + dxs[k], y + dys[k]

            if not in_range(nx, ny):
                continue
            if grid[nx][ny] == WALL:
                continue
            
            if visited[nx][ny] == -1:
                visited[nx][ny] = visited[x][y] + 1
                if type(grid[nx][ny]) != int and grid[nx][ny][1] == 'start':
                    result.append((visited[nx][ny], grid[nx][ny][0], nx, ny))
                que.append((nx, ny))
                
    result.sort(key = lambda x:(x[0], x[2], x[3]))
    return result
                        

def move_to_end(target):
    global now_fuel
    _, target_idx, target_x, target_y = target
    que = deque()
    visited = [[-1]*n for _ in range(n)]
    visited[target_x][target_y] = 0

    # return False 조건 
    # 1. 목적지까지 도달이 안되는 경우
    # 2. 목적지까지의 거리 - now_fuel < 0인 경우
    que.append((target_x, target_y))
    dist_to_end = -1
    while que:
        x, y = que.popleft()
        for k in range(4):
            nx, ny = x + dxs[k], y + dys[k]
            if not in_range(nx, ny):
                continue
            if grid[nx][ny] == WALL:
                continue
            if visited[nx][ny] == -1:
                visited[nx][ny] = visited[x][y] + 1
                if type(grid[nx][ny]) != int and grid[nx][ny][0] == target_idx and grid[nx][ny][1] == 'end':
                    dist_to_end = visited[nx][ny]
                que.append((nx, ny))
                
    if dist_to_end > -1:
        if now_fuel - dist_to_end < 0:
            return False
        # 정상적으로 운반이 가능할 경우
        now_fuel -= dist_to_end
        now_fuel += (dist_to_end*2)
        return True
    else:
        return False

def find_end_by_idx(idx):
    for i in range(n):
        for j in range(n):
            if type(grid[i][j]) != int and grid[i][j][0] == idx and grid[i][j][1] == 'end':
                return (i,j) 

done = 0 # 이동시킨 손님 수
while True:
    lst = find_shortest_pos() # 태울 타깃 
    
    if len(lst) > 0:
        # 택시 -> 손님 이동
        if now_fuel - lst[0][0] <= 0: # 택시 -> 손님 : 연료가 바닥나는 경우
            print(-1)
            break 
        else:
            now_fuel -= lst[0][0]
            taxi_x, taxi_y = lst[0][2], lst[0][3] # 택시-> 손님 : 택시 위치 업데이트
            # print("손님에게로,,택시 위치:",taxi_x,taxi_y, "연료 양:", now_fuel)
            if move_to_end(lst[0]): # 정상
                done += 1
                # print("목적지 도착,,, 연료 양:", now_fuel)
                
                if done == m:
                    print(now_fuel)
                    break
                taxi_nx, taxi_ny = find_end_by_idx(lst[0][1])
                taxi_x, taxi_y = taxi_nx, taxi_ny # 택시 위치 업데이트 : 최근 손님의 목적지
                # 완료한 손님은 빈칸 처리
                grid[lst[0][2]][lst[0][3]] = BLANK
                grid[taxi_x][taxi_y] = BLANK
            else: # 손님 출발지 -> 도착자 : 연료가 바닥나는 경우
                print(-1)
                break
    else:
        print(-1) # 모든 손님에게 도달하지 못하는 경우
        break


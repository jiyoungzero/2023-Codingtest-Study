import sys
import copy
input = sys.stdin.readline 
from collections import deque

# 1) 머리사람 방향으로 한 칸 이동
# 2) 공던지기(라운드에 따라 순서찾)
# 공의 순서(순환) :  왼쪽(행 증가 순), 아래(열 증가순), 오른쪽(행 감소), 위쪽(열 감소)
# 3) 점수 얻기
#    1. 공을 최초로 만나는 사람만 얻음(헤드에서 k번째 사람이라면: k*k)
#    2. 해당 팀의 헤드, 테일 바꾸고, 방향도 반대로
# 4) k번의 라운드만큼 하여 각 팀이 획득한 점수의 총합 구하기

# 0 : 빈칸
# 1 : 헤드
# 2 : 팀원
# 3 : 테일
# 4 : 팀의 이동선
n, m, k = map(int ,input().split())
answer = 0

arr = [list(map(int, input().split())) for _ in range(n)]
teams = [] # 
visited = [[False]*n for _ in range(n)]
dxs, dys = [1,-1,0,0], [0,0,1,-1]

def in_range(x, y):
    return 0 <= x < n and 0 <= y < n

def find_team(x, y):
    global tmp, visited
    if not in_range(x, y):return False
    if visited[x][y]:return False
    if arr[x][y] == 0: return False
    
    visited[x][y] = True
    tmp.append((x, y))  
    # 무조건 시계방향으로 먼저 찾기   
    find_team(x, y+1)
    find_team(x-1, y)
    find_team(x+1, y)
    find_team(x, y-1)
    return True

tmp = deque()
for i in range(n):
    for j in range(n):
        if not visited[i][j] and arr[i][j] != 0:
            tmp = deque()
            find_team(i, j)
            teams.append(tmp)

def define_team(team): # 초기 팀의 방향 알아내기 : 시계(1), 반시계(-1) -> [방향, 팀원들의 위치]
    h_idx = 0
    direction = 0
    team_pos = []

    for i, t in enumerate(team):
        x, y = t
        if arr[x][y] == 1:
            h_idx = i
            ni = (i+1)%len(team)
            nx, ny = team[ni]
            if arr[nx][ny] == 2:
                direction = 1
            else:
                direction = -1
            break

    if direction == 1: # rotate(1) -> 반시계로 돌릴 팀
        cur_i = h_idx
        while True:
            x, y = team[cur_i]
            if arr[x][y] == 3:
                team_pos.append(cur_i)
                break
            
            team_pos.append(cur_i)
            cur_i = (cur_i+1)%len(team)

    else:
        cur_i = h_idx
        while True:
            x, y = team[cur_i]
            if arr[x][y] == 3:
                team_pos.append(cur_i)
                break
            
            team_pos.append(cur_i)
            cur_i = (cur_i-1)%len(team) 
            
    return [direction, team_pos]

team_info = {}
for i, t in enumerate(teams):
    team_info[i] = define_team(t)

def move_team(team_idx, team_dir):
    team = teams[team_idx]
    team.rotate(team_dir)

    teams[team_idx] = team
    return 

def reverse_team(team_idx):
    team_info[team_idx][0] *= -1
    lst = team_info[team_idx][1]
    team_info[team_idx][1] = lst[::-1] # 머리-꼬리 위치 바꾸기
    return

def meet(x, y):
    for i in range(len(teams)):
        pos = team_info[i][1]
        for p_idx in range(len(pos)):
            tx, ty = teams[i][pos[p_idx]]
            if (tx, ty) == (x, y):
                # print("score (x, y)=", x, y)
                return [i, p_idx+1]
    return []


def throw_ball(time):
    score = 0
    time = time%(n*4)
    # print("----", time//n, time%n)
    if (time//n) == 0:
        row = time%n
        for j in range(n):
            x, y = row, j
            if arr[x][y] != 0 and len(meet(x, y)):
                idx, score = meet(x, y)
                break
    elif (time//n) == 1:
        col = time%n
        for i in range(n-1, -1, -1):
            x, y = i, col
            if arr[x][y] != 0 and len(meet(x, y)):
                idx, score = meet(x, y)
                break
    elif (time//n) == 2:
        row = (n-1) - time%n
        for j in range(n-1, -1, -1):
            x, y = row, j
            if arr[x][y] != 0 and len(meet(x, y)):
                idx, score = meet(x, y)
                break
    elif (time//n) == 3:
        col = (n-1) - time%n
        for i in range(n):
            x, y = i, col
            if arr[x][y] != 0 and len(meet(x, y)):
                idx, score = meet(x, y)
                break
    if score > 0:
        reverse_team(idx)
    return score*score

for time in range(k):
    for key, value in team_info.items():
        team_dir, team_pos = value
        move_team(key, team_dir)
        
    # print(team_info)
    answer += throw_ball(time) # 얻은 점수 리턴
    # print(time+1, "번째 턴 -> ", teams)
    # print(time+1, "번째 턴에 얻은 점수 =", answer)
    
    # print()

print(answer)
    
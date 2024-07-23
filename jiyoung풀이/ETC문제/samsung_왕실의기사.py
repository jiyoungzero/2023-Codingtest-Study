import sys
input = sys.stdin.readline 
from collections import deque

WALL = 2
BLANK = 0
TRAP = 1

l, n, q = map(int, input().split())
arr = [list(map(int, input().split())) for _ in range(l)]
warriers = {}
war_arr = [[-1]*l for _ in range(l)]
for idx in range(n):
    r, c, h, w, k = map(int, input().split())
    r-=1;c-=1
    war_arr[r][c] = idx
    warriers[idx] = [True, r, c , h, w, k, 0] # 살아있는지, 0 -> 데미지
cmds = [tuple(map(int, input().split())) for _ in range(q)] # i번 기사 : 방향 d로 한 칸 이동하라는

dxs, dys = [-1,0,1,0],[0,1,0,-1] # 위, 오른, 아래, 왼
answer = 0 

def outter_wall(x, y):
    return x < 0 or l <= x or y < 0 or l <= y

def meet(x, y, idx):
    for k, v in warriers.items():
        if not v[0]: continue # 이미 죽은 워리어
        sr, sc = v[1], v[2]
        h, w = v[3], v[4]
        for i in range(sr, sr + h):
            for j in range(sc, sc + w):
                if idx != k and x == i and y == j:
                    return k
    return -1

def get_chains(idx, d):
    chains = set() # 연쇄적으로 밀리는 기사들

    que = deque()
    que.append(idx)
    while que:
        now = que.popleft()
        target = warriers[now]
        sx, sy = target[1], target[2]
        h, w = target[3], target[4]
        push_lst = []
        for x in range(sx, sx + h):
            for y in range(sy, sy + w):
                nx, ny = x + dxs[d], y + dys[d]
                push_lst.append((nx, ny))

        # 현재 기사가 벽을 마주하지 않고 다른 기사를 미는지
        wall_flag = False
        mt_set = set()
        for x, y in push_lst:
            mt =  meet(x, y, now)
            if outter_wall(x, y) or arr[x][y] == WALL :
                wall_flag = True
                break
            elif mt >= 0:
                mt_set.add(mt)
        if wall_flag: # 중간에 벽을 만나면 전체가 움직이지 못함
            chains = set() 
            break

        else:
            chains.add(now)
            for m_idx in list(mt_set):
                que.append(m_idx)
                chains.add(m_idx)

    return list(chains)

def get_damage(idx):
    sx, sy = warriers[idx][1], warriers[idx][2]
    h, w = warriers[idx][3], warriers[idx][4]

    result = 0
    for i in range(sx, sx + h):
        for j in range(sy, sy + w):
            if arr[i][j] == TRAP:result += 1
    return result
                
def warriers_move(targets, d, start):
    global warriers
    damages = {}
    for i, target in enumerate(targets):
        r, c = warriers[target][1], warriers[target][2]
        warriers[target][1] = r + dxs[d]
        warriers[target][2] = c + dys[d]        
        if target != start:
            damage = get_damage(target)
            # print(target+1, "기사의 데미지 :", damage)
            damages[target] = damage

    
    for k, dam in damages.items():
        warriers[k][-1] += dam
        warriers[k][-2] -= dam
        if warriers[k][-2] <= 0:
            warriers[k][0] = False
    
    
    

for t, (i, d) in enumerate(cmds):
    
    lst = get_chains(i-1, d)
    if len(lst):
        print("chains", lst)
        warriers_move(lst, d, i-1)

    print(warriers)
    print()
    
def get_answer():
    global answer
    for k, v in warriers.items():
        if v[0]:
            answer += v[-1]
    return answer

print(get_answer())

import sys
input = sys.stdin.readline 
import copy
from collections import deque

n, m = map(int, input().split())
arr = [list(map(int, input().split())) for _ in range(n)]
attacks = [tuple(map(int, input().split())) for _ in range(m)]
dxs, dys = [0, 1, 0, -1], [1, 0, -1, 0]
answer = 0

def in_range(x, y):
    return 0 <= x < n and 0 <= y < n

def attack_monster(d, p):
    global answer
    x, y = n//2, n//2
    for _ in range(p):
        nx, ny = x + dxs[d], y + dys[d]
        if not in_range(nx, ny):break
        answer += arr[nx][ny]
        arr[nx][ny] = 0
        x, y = nx, ny


def in_pop_lst(idx, pop_lst):
    for start, end in pop_lst:
        if start <= idx < end:
            return True
    return False

def arr2line():
    m_dxs, m_dys = [0, 1, 0, -1], [-1, 0, 1, 0]
    cur_x, cur_y = n//2, n//2
    move_dir, move_num = 0, 1
    lst = []

    while cur_x or cur_y:
        for _ in range(move_num):
            cur_x += m_dxs[move_dir]
            cur_y += m_dys[move_dir]
            if arr[cur_x][cur_y] != 0:
                lst.append(arr[cur_x][cur_y])

            # 이동 중에 (0, 0)으로 오게 된다면 종료
            if (cur_x, cur_y) == (0, 0):
                break
        move_dir = (move_dir+1)%4
        if move_dir == 0 or move_dir == 2:
            move_num += 1
    return lst


def popping(lst):
    global arr, answer
    n_arr = [[0]*n for _ in range(n)]

    pop_lst = []
    pop_flag = False
    prefix = lst[0]
    dup = 1
    for i, ele in enumerate(lst[1:]):
        if ele == prefix:
            dup += 1
        else:
            if dup >= 4:
                pop_flag = True
                pop_lst.append((i-dup+1, min(len(lst), i+1)))
                answer += (prefix*dup)
            dup = 1
        prefix = ele

    final_lst = []
    for i, ele in enumerate(lst):
        if in_pop_lst(i, pop_lst):continue
        final_lst.append(ele)

    return (final_lst, pop_flag)
    

def line2arr(final_lst): 
    global arr
    n_arr = [[0]*n for _ in range(n)]
    que = deque(final_lst)

    m_dxs, m_dys = [0, 1, 0, -1], [-1, 0, 1, 0]
    cur_x, cur_y = n//2, n//2
    move_dir, move_num = 0, 1

    while cur_x or cur_y:
        for _ in range(move_num):
            if cur_x == 0 and cur_y == 0:break
            if not que:break
            
            cur_x += m_dxs[move_dir]
            cur_y += m_dys[move_dir]

            ele = que.popleft()
            n_arr[cur_x][cur_y] = ele
        move_dir = (move_dir + 1)%4
        if move_dir%2 == 0: move_num += 1
        if not que:break

    # arr 업데이트
    arr = copy.deepcopy(n_arr)


def get_input_arr(lst):
    nxt_lst = []
    if lst[-1] != 0:
        lst.append(0)
    cnt = 1
    prefix = lst[0]
    for i, ele in enumerate(lst[1:]):
        if ele == prefix:
            cnt += 1
        else:
            nxt_lst.append(cnt)
            nxt_lst.append(prefix)
            cnt = 1
        prefix = ele 
    return nxt_lst


for time in range(m):
    d, p = attacks[time]
    attack_monster(d, p)
    lst = arr2line()

    while True:
        lst.append(0)
        nxt_lst, flag = popping(lst)
        if not flag:
            break
        lst = nxt_lst
    
    line2arr(get_input_arr(lst))


print(answer)

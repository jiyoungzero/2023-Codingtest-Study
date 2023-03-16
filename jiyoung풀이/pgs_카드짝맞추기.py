# 구현 
# 이거는 무조건 최소 5번은 풀어야 함 ㅇㅋ? -> 

from collections import deque
from itertools import permutations
from copy import deepcopy

board = []
def ctrl_move(r, c, k, t):
    global board
    while True:
        nr, nc = r+k, c+t
        if not (0<=nr<4 and 0<=nc<4):
            return r, c
        if board[nr][nc] != 0:
            return nr, nc
        r, c = nr, nc

def bfs(start, end):
    r, c = start
    s_r, s_c = end
    que = deque()
    que.append((r,c, 0))
    visited = [[0]*4 for _ in range(4)]
    move = [(0,1),(0,-1),(1,0),(-1,0)]
    while que:
        r, c, tmp = que.popleft()
        if visited[r][c] : continue
        visited[r][c] = 1
        if r == s_r and c == s_c:return tmp
        for k, t in move:
            nr, nc = r + k, c+t
            if 0<=nr<4 and 0<=nc<4:
                que.append((nr, nc, tmp+1))
            nr, nc = ctrl_move(r, c, k, t)
            que.append((nr, nc, tmp+1))
    return -1
            

def solution(input_board, input_r, input_c):
    answer = int(1e9)
    global board
    card_info = [[] for i in range(7)]
    nums = []
    
    for i in range(4):
        for j in range(4):
            if input_board[i][j]:
                if input_board[i][j] not in nums:nums.append(input_board[i][j])
                card_info[input_board[i][j]].append((i,j))
    per = list(permutations(nums, len(nums)))
    
    for i in range(len(per)):
        board = deepcopy(input_board)
        cnt = 0
        r, c = input_r, input_c
        for j in per[i]:
            left = bfs((r, c), card_info[j][0])
            right = bfs((r,c), card_info[j][1])
            if left < right:
                cnt += left
                cnt += bfs(card_info[j][0], card_info[j][1])
                r, c = card_info[j][1]
                
            else:
                cnt += right
                cnt += bfs(card_info[j][1], card_info[j][0])
                r, c = card_info[j][0]
                
            board[card_info[j][0][0]][card_info[j][0][1]], board[card_info[j][1][0]][card_info[j][1][1]] = 0,0
            cnt += 2 #뒤집기 2번
        answer = min(answer, cnt)
    
    return answer
# 구현 0: 위쪽, 1: 오른쪽, 2: 아래, 3: 왼쪽쪽

import sys
input = sys.stdin.readline

n, m = map(int, input().split())
a, b, d = map(int, input().split()) # 0: 육지, 1:바다

arr = [list(map(int, input().split())) for _ in range(n)]
n_move = [(0, -1), (1, 0), (0, 1), (-1, 0)] # 0
e_move = [(-1,0), (0, -1), (1,0), (0, 1)] # 1
s_move = [(0,1), (-1, 0), (0, -1), (1, 0)] # 2
w_move = [(1, 0), (0, 1), (-1, 0), (0, -1)] # 3
move = []

if d == 0: 
    move = n_move
elif d == 1: 
    move = e_move
elif d == 2 : 
    move = s_move
elif d == 2 : 
    move = w_move
flag = True
cnt = 1
m_cnt = 1

while m_cnt != 4:
    m_cnt = 0
    arr[a][b] = 1 # visitied 표시
    for m in move:
        na, nb = a+m[0], b+m[1]
        if arr[na][nb] == 1:
            m_cnt += 1
            # continue
        else: 
            a, b = na, nb
            cnt += 1
            m_cnt = 0 # reset
            arr[na][nb] = 1 # visited표시
print(cnt)
    
        
     
    
        


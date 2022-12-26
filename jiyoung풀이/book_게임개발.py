# 구현 0: 위쪽, 1: 오른쪽, 2: 아래, 3: 왼쪽쪽

# import sys
# input = sys.stdin.readline

# n, m = map(int, input().split())
# a, b, d = map(int, input().split()) # 0: 육지, 1:바다

# arr = [list(map(int, input().split())) for _ in range(n)]
# n_move = [(0, -1), (1, 0), (0, 1), (-1, 0)] # 0
# e_move = [(-1,0), (0, -1), (1,0), (0, 1)] # 1
# s_move = [(0,1), (-1, 0), (0, -1), (1, 0)] # 2
# w_move = [(1, 0), (0, 1), (-1, 0), (0, -1)] # 3
# move = []

# if d == 0: 
#     move = n_move
# elif d == 1: 
#     move = e_move
# elif d == 2 : 
#     move = s_move
# elif d == 2 : 
#     move = w_move
# flag = True
# cnt = 1
# m_cnt = 1

# while m_cnt != 4:
#     m_cnt = 0
#     arr[a][b] = 1 # visitied 표시
#     for m in move:
#         na, nb = a+m[0], b+m[1]
#         if arr[na][nb] == 1:
#             m_cnt += 1
#             # continue
#         else: 
#             a, b = na, nb
#             cnt += 1
#             m_cnt = 0 # reset
#             arr[na][nb] = 1 # visited표시
# print(cnt)

# 모범답안

n, m = map(int, input().split())
visited = [[0]*m for _ in range(n)]
x, y, d = map(int, input().split())

visited[x][y] = 1 # 현재 위치 방문 처리

arr = [list(map(int, input().split())) for _ in range(n)]

dx, dy = [-1, 0, 1, 0], [0, 1, 0, -1] # 동 서 남 북 방향

# 왼쪽으로 회전
def turn_left():
    global d
    d -= 1
    if d == -1: d = 3
    
cnt = 1
m_cnt = 0
while True:
    turn_left()
    nx, ny = x+dx[d], y +dy[d]
    if visited[nx][ny] == 0 and arr[nx][ny] == 0:
        visited[nx][ny] = 1
        cnt +=1
        m_cnt = 0
        x, y = nx, ny
        continue
    else: m_cnt += 1        

    if m_cnt == 4: # 모두 갈 수 없는 경우에는 뒤로 갈 수 있나 확인, 뒤도 막히면 break --> 이 부분 구현 못함
        nx, ny = x - dx[d], y - dy[d]
        
        if arr[nx][ny] == 0:
            x, y = nx, ny
        else:
            break
        m_cnt = 0 
     
print(cnt)
    
        


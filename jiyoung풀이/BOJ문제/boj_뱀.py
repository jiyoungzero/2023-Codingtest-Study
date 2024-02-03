import sys
input = sys.stdin.readline 

n = int(input())
apple = [[False]*n for _ in range(n)]
k = int(input()) # 사과의 개수
answer = 0
for _ in range(k):
    r, c = map(int, input().split())
    apple[r-1][c-1] = True
    
L = int(input())
dir_cmds = []

for _ in range(L):
    x, c = map(str, input().split())
    dir_cmds.append((int(x), c)) # L이면 반시계 방향으로, D은 시계방향으로 
now_dir = 0
snake = [(0,0)]

def is_twisted(nx, ny):
    return (nx, ny) in snake

def can_go(x, y):
    return 0 <= x < n and 0 <= y < n

def push_head(nx, ny):
    if is_twisted(nx, ny):
        return False

    snake.insert(0, (nx, ny))
    return True

def pop_tail():
    snake.pop()

def move_snake(nx, ny):
    if apple[nx][ny]:
        apple[nx][ny] = False
        if not push_head(nx, ny):
            return False
    else:        
        if not push_head(nx, ny):
            return False
        pop_tail()

    return True
        

def need_to_change_dir():
    if dir_cmds and answer == dir_cmds[0][0]+1:
        return True
    return False
    
def move():
    global answer, now_dir
    dxs, dys = [0, 1, 0, -1],[1, 0, -1, 0] # R, D, L, U 
    # print("time=",answer, snake)
    answer += 1 
    
    # 방향 전환 
    if need_to_change_dir():
        nxt_ = dir_cmds.pop(0)
        if nxt_[1] == 'D': 
            now_dir = (now_dir+1)%4
        else:
            if now_dir == 0:
                now_dir = 3
            else:  
                now_dir = (now_dir-1)
    x, y = snake[0]
    nx, ny = x + dxs[now_dir], y + dys[now_dir]
    
    if not can_go(nx, ny):
        return False
    if not move_snake(nx, ny):
        return False
    
    return True



while True:
    if not move():
        break
print(answer)






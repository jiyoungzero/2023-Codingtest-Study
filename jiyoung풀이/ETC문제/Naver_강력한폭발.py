# backtracking

n = int(input())
maze = [list(map(int, input().split())) for _ in range(n)]
bomb_pos = []
for i in range(n):
    for j in range(n):
        if maze[i][j] == 1:
            bomb_pos.append((i,j))
bomb_command = {0:[(1,0),(-1,0),(2,0),(-2,0)], 1:[(1,0),(-1,0),(0,1),(0,-1)], 2:[(-1,-1),(1,-1),(1,1),(-1,1)]}
answer = 0

def get_area():
    global answer
    result = 0
    for i in range(n):
        for j in range(n):
            if maze[i][j]:
                result += 1
    answer = max(answer, result)

def in_range(a, b):
    return 0<=a<n and 0<=b<n

def bomb(b_cnt, idx, action):
    x, y = bomb_pos[b_cnt][0], bomb_pos[b_cnt][1]
    
    factor = 1 if action == 'do' else -1
    for k in bomb_command[idx]:
        nx, ny = x+k[0], y+k[1]
        if not in_range(nx, ny):continue
        maze[nx][ny] += factor

def soltuion(b_cnt):
    if b_cnt == len(bomb_pos):
        get_area()
        return 
    
    for i in range(3):
        bomb(b_cnt, i, 'do')
        soltuion(b_cnt+1)
        bomb(b_cnt, i, 'undo')
        
soltuion(0)
print(answer)
        
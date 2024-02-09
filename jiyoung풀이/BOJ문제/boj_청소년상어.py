import sys, copy
input = sys.stdin.readline

grid = []
dxs, dys = [-1,-1,0,1,1,1,0,-1],[0,-1,-1,-1,0,1,1,1]
answer = 0

for _ in range(4):
    a1, b1, a2, b2, a3, b3, a4, b4 = map(int, input().split())
    grid.append([(a1, (b1-1)%8), (a2, (b2-1)%8), (a3, (b3-1)%8), (a4, (b4-1)%8)])

def in_range(x, y):
    return 0 <= x < 4 and 0 <= y < 4

def find_pos(grid, num):
    for i in range(4):
        for j in range(4):
            if grid[i][j] != 0 and grid[i][j][0] == num:
                return (i, j)
    return False

def can_move(x, y, dir, shark_pos):
    nx, ny = x + dxs[dir], y + dys[dir]
    if not in_range(nx, ny):
        return False
    if (nx, ny) == shark_pos:
        return False
    return True

def move(grid, x, y, shark_pos):
    cur_dir = grid[x][y][1]
    if can_move(x, y, cur_dir, shark_pos):
        nx, ny = x + dxs[cur_dir], y + dys[cur_dir]
        grid[x][y], grid[nx][ny] = grid[nx][ny], grid[x][y]
    else:
        while True:
            cur_dir = (cur_dir + 1)%8
            if can_move(x, y, cur_dir, shark_pos):
                grid[x][y] = (grid[x][y][0], cur_dir) # 반시계 방향으로 업데이트
                nx, ny = x + dxs[cur_dir], y + dys[cur_dir]
                grid[x][y], grid[nx][ny] = grid[nx][ny], grid[x][y]
                break
    

def move_fish_all(grid, shark_pos):
    for num in range(1, 17):
        fish_pos = find_pos(grid, num)
        if fish_pos != False:
            x, y = fish_pos
            move(grid, x, y, shark_pos) # 개별로 이동

def get_edible_lst(grid, shark_pos, shark_dir):
    lst = []
    x, y = shark_pos
    for _ in range(4):
        x += dxs[shark_dir]
        y += dys[shark_dir]
        if not in_range(x, y):
            continue
        if grid[x][y] != 0: # 물고기가 있을 때
            lst.append((x, y))
    return lst

def dfs(grid, shark_pos, total):
    global answer 
    grid = copy.deepcopy(grid)
    
    # 현재 위치에 있는 물고기를 먼저 먹고
    x, y = shark_pos
    total += grid[x][y][0]
    shark_dir = grid[x][y][1]
    grid[x][y] = 0 # 물고기 먹기

    # 모든 물고기를 이동시킴
    move_fish_all(grid, shark_pos)

    
    # 현재 상어 위치에서 먹을 수 있는 물고기 리스트를 반환 
    edible_lst = get_edible_lst(grid, shark_pos, shark_dir)
    if len(edible_lst) == 0:
        answer = max(answer, total)
        return 
    for nx, ny in edible_lst: # 모든 이동할 수 있는 위치로 재귀적으로 수행
        dfs(grid, (nx, ny), total)
    
dfs(grid, (0,0), 0)
print(answer)

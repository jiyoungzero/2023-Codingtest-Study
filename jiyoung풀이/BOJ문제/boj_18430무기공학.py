import sys
input = sys.stdin.readline 

n, m = map(int ,input().split())
arr = [list(map(int, input().split())) for _ in range(n)]
answer = 0

dirs = [[(0,-1),(0,0),(1,0)], [(-1,0),(0,0),(0,-1)], [(-1,0),(0,0),(0,1)],[(0,0),(0,1),(1,0)]]
def in_range(x, y):
    return 0 <= x < n and 0 <= y < m


used = [[False]*m for _ in range(n)]
def backtracking(x, y, sel):
    global answer
    if x == n and y == m:
        answer = max(answer, sel)
        return
    if y == m:
        nx, ny = x+1, 0
    else:
        nx, ny = x, y+1
    
    # 선택 안하는 경우
    backtracking(nx, ny, sel)
    
    # # 이미 선택이 된 경우
    # if used[nx][ny]:
    #     backtracking(nx, ny, sel)    
        
    # 선택하는 경우
    for dir in dirs:
        flag = True
        for kx, ky in dir:
            nnx, nny = nx + kx, ny+ky
            if not in_range(nnx, nny) or used[nnx][nny]:
                flag = False 
                break 
        if flag:
            plus = 0
            for dx, dy in dir:
                nnx, nny = nx + dx, ny + dy
                used[nnx][nny] = True
                if dx == 0 and dy == 0:
                    plus += (2*arr[nnx][nny])
                else:
                    plus += (arr[nnx][nny])
                    
            backtracking(nx, ny, sel+plus)
            for dx, dy in dir:
                nnx, nny = nx + dx, ny + dy
                used[nnx][nny] = False
            flag = True

backtracking(0,0,0)
print(answer)
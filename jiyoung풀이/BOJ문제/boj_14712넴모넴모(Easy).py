import sys
input = sys.stdin.readline 

n, m = map(int, input().split())
board = [[0]*(m+1) for _ in range(n+1)]
answer = 0

def backtracking(x, y):
    global answer
    if x==(n+1) and y == 1:
        answer += 1
        return 
    if y == m:
        nx, ny = x+1, 1
    else:
        nx, ny = x, y+1
    # 선택하지 않는 경우
    backtracking(nx, ny)
    
    # 선택하는 경우
    if board[x-1][y-1] == 0 or board[x-1][y] == 0 or board[x][y-1] == 0:
        board[x][y] = 1
        backtracking(nx, ny)
        board[x][y] = 0
    

backtracking(1, 1)
print(answer)
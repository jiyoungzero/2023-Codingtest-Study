def solution(board):
    answer = 0
    dx, dy = [0,0,1,-1],[1,-1,0,0]
    s_x, s_y = 0,0
    r, c = len(board), len(board[0])
    
    for i in range(r):
        for j in range(c):
            if board[i][j] == "R":
                s_x, s_y = i, j
                break
    
    
    
    
    return answer
def solution(n, m, pos, arr):
    result = 0
    # 0: 북쪽, 1: 동쪽, 2:남쪽, 3:서쪽
    # 0 : 육지, 1: 바다
    start, dir = [pos[0], pos[1]], pos[2]
    dx, dy = [-1,0,1,0],[0,1,0,-1] # 북동남서
    visited = [[False]*m for _ in range(n)]
    
    
    
    return result
print(solution(4,4,[1,1,0],[[1,1,1,1],[1,0,0,1],[1,1,0,1],[1,1,1,1]]))

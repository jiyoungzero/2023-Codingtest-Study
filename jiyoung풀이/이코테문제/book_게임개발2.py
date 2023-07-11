

def solution(n, m, pos, arr):
    result = 0
    # 0: 북쪽, 1: 동쪽, 2:남쪽, 3:서쪽
    # 0 : 육지, 1: 바다
    x, y, dir = pos[0], pos[1], pos[2]
    dx, dy = [-1,0,1,0],[0,1,0,-1] # 북동남서
    visited = [[False]*m for _ in range(n)]
    
    # 첫위치 방문처리
    visited[x][y] = True
    
    def turn_left():
        dir -= 1
        if dir == -1:
            dir = 3
        return dir

    turn_time = 0
    while True:
        turn_left()
        nx = x + dx[dir]
        ny = y + dy[dir]
        
        # 회전한 경우 정면에 가보지 않았거나 칸이 존재한느 경우
        if not visited[nx][ny] and arr[nx][ny] == 0:
            visited[nx][ny] = True
            turn_left()
            x, y = nx, ny
            result += 1
            turn_time = 0
            continue
        
        else:# 회전한 이후 다 가보았거나, 바다인 경우
            turn_time += 1
            
            
        # 네 방향 모두 갈 수 없는 경우
        if turn_time == 4:
            nx, ny  = x - dx[dir], y - dy[dir]
            turn_time = 0
            
            # 뒤로 갈 수 있으면 이동, 아니면 break
            if arr[nx][ny] == 0:
                x, y = nx, ny
            else:
                break
            

    return result
print(solution(4,4,[1,1,0],[[1,1,1,1],[1,0,0,1],[1,1,0,1],[1,1,1,1]]))

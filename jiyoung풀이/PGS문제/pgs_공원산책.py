# 정확성 75/100 -> 다시..

def solution(park, routes):
    answer = []
    r, c = len(park), len(park[0])
    x, y = 0,0
    for i in range(r):
        for j in range(c):
            if park[i][j] == "S":
                x, y = i, j
                break
                
    
    for route in routes:
        flag = False
        cmd = list(route.split(" "))
        move = int(cmd[1])
        
        if cmd[0] == "E":
            nx, ny = x, y+move
            if nx<0 or r<=nx or ny<0 or c<=ny:
                    continue
            for i in range(y, ny+1):
                if park[nx][i] == "X":
                    flag = True
                    break
                
        elif cmd[0] == "W":
            nx, ny = x, y-move
            if nx<0 or r<=nx or ny<0 or c<=ny:
                    continue
            for i in range(ny, y-1, -1):
                if park[nx][i] == "X":
                    flag = True
                    break
                
        elif cmd[0] == "S":
            nx, ny = x+move, y
            if nx<0 or r<=nx or ny<0 or c<=ny:
                    continue
            for i in range(x, nx+1):
                if park[i][ny] == "X":
                    flag = True
                    break
                
        elif cmd[0] == "N":
            nx, ny = x-move, y
            if nx<0 or r<=nx or ny<0 or c<=ny:
                    continue
            for i in range(nx, x-1, -1):
                if park[i][ny] == "X":
                    flag = True
                    break
        if not flag:
            x, y = nx, ny
    answer = [x,y]
            
            
    return answer
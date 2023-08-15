# 구현 
# 삼전 코테 

import sys
input = sys.stdin.readline

n = int(input())
k = int(input())
data = [[0]*100 for _ in range(100)]

for _ in range(k):
    a, b = map(int, input().split())
    data[a][b] = 1 # 사과있음 

l = int(input())
info = []
for _ in range(l):
    x, c = input().split()
    info.append([int(x), c])

# 동 남 서 북
dx, dy = [0,1,0,-1],[1,0,1,0]

# 방향 바꾸기 함수
def turn(dir, c):
    if c == "L":
        dir = (dir-1)%4
    else:
        dir = (dir+1)%4
    return dir
    
# 시뮬레이션 함수
def simulate():
    x, y = 1,1 # 현재 위치
    data[x][y] = 2 # 뱀 위치는 2
    direction = 0 # 처음에는 동쪽
    time = 0 # 시작한 후에 지난 시간
    nxt = 0 # 다음에 회전할 정보
    q = [(x, y)] # 뱀이 차지하는 위치 정보 (꼬리가 앞)

    while 1:
        nx, ny = x+dx[direction], y + dy[direction]
        
        if 1<=nx<=n and 1<=ny<=n and data[nx][ny] != 2:
            # 사과가 없으면 이동 후에 꼬리 제거
            if data[nx][ny]  != 1:
                data[nx][ny] = 2
                q.append((nx,ny))
                px, py = q.pop()
                data[px][py] = 0
            # 사과가 있으면 이동 후에 꼬리 그대로 두기
            if data[nx][ny] == 1:
                data[nx][ny] = 2
                q.append((nx,ny))
        
        else:
            time+=1
            break
        x, y = nx, ny
        time += 1
        
        # 회전할 시간인 경우 회전
        if nxt < 1 and time == info[nxt][0]:
            direction = turn(direction, info[nxt][1])
            nxt += 1
    
    return time

print(simulate())
                
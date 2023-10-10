# 구현 + bfs

from collections import deque
n = int(input())
arr = [list(map(int, input().split())) for _ in range(n)]
dx, dy = [0,0,-1,1],[1,-1,0,0]
shark = (0,0) # 상어 위치
weight = 2 # 상어 현재 크기
fish = [] # (x좌표, y좌표, 크기)
time = 0


for i in range(n):
    for j in range(n):
        if arr[i][j] == 9:
            shark = (i,j)
            break
        

q = deque() # 상어 경로
q.append((shark))

# 먹을 수 있는 물고기 
def search():
    s_x, s_y = q.popleft()
    for k in range(4):
        ns_x, ns_y = s_x+dx[k], s_y+dy[k]
        if 0<=ns_x<n and 0<=ns_y<n:
            if arr[ns_x][ns_y]: # 지나갈 수 있음
                q.append((ns_x,ns_y))
                if arr[ns_x][ns_y] < weight: # 먹을 수 있음
                    fish.append([ns_x, ns_y,arr[ns_x][ns_y]])  
    return sorted(fish, key=lambda x:(x[0], x[1]))


# 섭취하면서 크기 키우기
def eat():
    global time, weight
    while True:
        result = search() # 먹은 물고기
        if len(result) == 0:
            return time
        
        plus =  len(result) // weight
        
        weight += plus
        time += 1

print(eat())
    
    


# 구현, bfs
import sys
from collections import deque
input =sys.stdin.readline


'''
지나갈 수 있는 조건: 아기상어(9) >= 물고기
먹을 수 있는 조건: 아기상어 > 물고기

먹으러 이동할 때 조건
1. 가장 가까운 경로로 가기
2. 왼쪽/위 순으로 먹기

몸무게: 아기상어 += 1
시간 : 이동시간만 취급


<풀이>
1. 물고기 정보 담은 배열 생성 (몸무게, (x,y))
2. 현재 아기상어의 위치와 몸무게를 담은 deque 생성 
    거리상으로 위/왼쪽에 있는 것부터 pop() / x값이 아기상어의 x보다 작고 y의 값이 작을 수록
3. 해당 위치까지 갈 때 아기상어보다 같거나 큰 물고기가 있다면 bfs돌려서 돌아가기
4. 해당 위치까지 가는 동안 time + 1  
5. 물고기 먹으면 weight += 1
6. 다음 물고기 장소로 가는 거 3번부터 반복
'''
n = int(input())
arr = [list(map(int ,input().split())) for _ in range(n)]
shark_weight = 2
cur_x, cur_y = 0,0
dxs, dys = [0,0,1,-1], [1,-1,0, 0]

for i in range(n):
    for j in range(n):
        if arr[i][j] == 9:
            cur_x, cur_y = i, j
            arr[i][j] = 0 # 상어 위치값 초기화하기 -> 나중에 탐색할 때 불편할까봐

def bfs(x, y): # 현재 위치에서 bfs돌면서 지나갈 수 있는 물고기를 q에 넣고 return 
    # 현재 위치에서 가는 경우를 여러번 돌려야 하니까 여기서 초기화
    visited = [[False]*n for _ in range(n)]
    distance = [[0]*n for _ in range(n)]
    
    q = deque([(x, y)]) # 현재 아기상어의 위치
    visited[x][y] = True
    fish_lst = []
    while q:
        x, y = q.popleft()
        for i in range(4):
            nx,ny = x+dxs[i], y+dys[i]
            if (0<=nx<n and 0<=ny<n) and not visited[nx][ny]:
                if shark_weight >= arr[nx][ny]: # 지나갈 수 있을떼,
                    distance[nx][ny] = distance[x][y] + 1
                    visited[nx][ny] = True # 여기에서 처리하는게 맞나?
                    q.append((nx, ny))
                    if 0< arr[nx][ny] < shark_weight:
                        fish_lst.append((nx, ny, distance[nx][ny]))
    return sorted(fish_lst, key=lambda x:(-x[2],-x[0],-x[1]))

fish_cnt = 0
time = 0
while 1:
    fish = bfs(cur_x, cur_y)
    
    if len(fish) == 0:
        break
    
    # 물고기 꺼내다가 shark_weight랑 같아지면 몸무게 증가시키기
    fish_x, fish_y, dist = fish.pop()
    time += dist
    fish_cnt += 1
    
    # 아기상어 위치 갱신
    cur_x, cur_y = fish_x, fish_y
    
    # 먹은 물고기는 위치 0
    arr[fish_x][fish_y] = 0
    
    if fish_cnt == shark_weight:
        shark_weight += 1
        fish_cnt = 0 
        
print(time)
    
            
            
            
        

        
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
    
    
    
# 다른 풀이 (이코테)
from collections import deque
INF = int(1e9)

n = int(input())

arr = []
for i in range(n):
    arr.append(list(map(int, input().split())))
    
# 아기상어의 현재크기, 현재 위치 변수
now_size = 2
now_x, now_y = 0,0

for i in range(n):
    for j in range(n):
        if arr[i][j] == 9:
            now_x, now_y = i,j
            arr[i][j] = 0
dx,dy = [-1,0,1,0], [0,1,0,-1]

# 모든 위치까지의 최단거리만! 계산하는 bfs함수
def bfs():
    dist = [[-1]*n for _ in range(n)] # 값이 -1이라면 도달할 수 없음으로 초기화
    q = deque([(now_x, now_y)])
    dist[now_x][now_y] = 0
    while q:
        x, y = q.popleft()
        for i in range(4):
            nx, ny = x+dx[i], y+dy[i]
            if 0<=nx<n and 0<=n<n:
                # 지나갈 수 있는 경우
                if dist[nx][ny] == -1 and arr[nx][ny] <= now_size:
                    dist[nx][ny] = dist[x][y] + 1
                    q.append((nx, ny))
    return dist # 모든 위치까지의 최단 거리 테이블 반환

# 먹을 물고기를 찾는 함수
def find(dist):
    x, y = 0,0
    min_dist = INF
    for i in range(n):
        for j in range(n):
            # 도달이 가능하면서 먹을 수 있는 물고기
            if dist[i][j] != -1 and 1 < arr[i][j] < now_size:
                if dist[i][j] < min_dist: # 가장 가까운 물고기 한마리만 선택하기 위해
                    x, y = i, j
                    min_dist = dist[x][y]
    if min_dist == INF: # 먹을 물고기가 없으면
        return None
    else:
        return x, y, min_dist
    
result = 0 # 최종 답안
ate = 0 # 현재 크기에서 먹은 양

while 1:
    # 먹을 수 있는 물고기와 위치 찾기 
    value = find(bfs())
    
    if value == None:
        print(result)
        break
    else:
        # 현재 위치 갱신하고 이동 거리 변경
        now_x, now_y = value[0], value[1]
        result += value[2]
        
        # 먹은 물고기는 아무것도 없게 처리
        arr[now_x][now_y] = 0
        ate += 1
        
        if ate>=now_size:
            now_size += 1
            ate = 0
                
            
            
            
            
        

        
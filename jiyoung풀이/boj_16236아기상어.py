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
arr = [list(map(int, input().split())) for _ in range(n)]
dxs, dys = [1,1,0,0],[0,0,-1,1] 
shark_x, shark_y = 0,0


for i in range(n):
    for j in range(n):
        if arr[i][j] == 9:
            shark_x, shark_y = i,j
            arr[i][j] = 0 # 상어 위치는 초기화

def bfs(x, y, weight):
    q = deque([(x, y)])
    distance = [[0]*n for _ in range(n)]
    visited = [[False]*n for _ in range(n)]
    visited[x][y] = True
    tmp = []
    
    while q: # 인접한 곳에 없을 경우가 있어서 일단 지나갈 수 있는 위치는 무조건 q에 저장
        cur_x, cur_y = q.popleft()
        for i in range(4):
            nx, ny = cur_x+dxs[i], cur_y+dys[i]
            if (0<=nx<n and 0<=ny<n) and not visited[nx][ny]:
                if arr[nx][ny] <= weight: # 지나갈 수 있으면
                    visited[nx][ny] = True
                    q.append((nx, ny))
                    distance[nx][ny] = distance[cur_x][cur_y] + 1 # 최단 경로(bfs)
                    if 0 < arr[nx][ny] < weight : # 먹을 수 있으면
                        tmp.append((nx, ny, distance[nx][ny]))
                        
    return sorted(tmp, key=lambda x:(-x[2], -x[0], -x[1])) 

weight = 2
result = 0
fish_cnt = 0
while 1:
    fish = bfs(shark_x, shark_y, weight)
    
    if len(fish) == 0:
        break
    
    else:
        # 정렬된 물고기를 하나씩 꺼내다가 weight랑 같을 때 +1
        nx, ny, dist = fish.pop() 
        result += dist
        # 먹은 물고기는 없어지니까
        arr[nx][ny] = 0
        arr[shark_x][shark_y] = 0
        # 아기상어 위치 업데이트, 이동한 만큼 result에 더하기
        shark_x, shark_y = nx, ny
        
        fish_cnt += 1
        
        if fish_cnt == weight:
            weight += 1
            fish_cnt = 0
print(result)
        

        
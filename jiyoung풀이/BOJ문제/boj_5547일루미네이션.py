import sys
input = sys.stdin.readline
from collections import deque 

# 전체 좌표 평면의 외곽에 1만큼의 여백을 추가하고 x,y 좌표가 0부터 시작한다고 판단
# y가 홀수 일 때, 인접한 좌표는 상하좌우와 함께 우상단,우하단을 포함
# y가 짝수 일 때, 인접한 좌표는 상하좌우와 함께 좌상단, 좌하단을 포함
# 건물이 없는 좌표를 BFS 탐색하면서 건물과 만나는 지점을 카운트

w, h = map(int, input().split())
arr = [list(map(int, input().split())) for _ in range(h)]
answer = 0
dxs, dys = [-1, 0, 1, 0, -1, -1], [-1, -1, 0, 1, 1, 0 ]
visited = [[False]*w for _ in range(h)]

def bfs(x, y):
    global answer
    que = deque()
    visited[x][y] = True
    que.append((x, y))
    
    while que:
        x, y = que.popleft()
        for k in range(6):
            nx, ny = x + dxs[k], y + dys[k]
            if nx < 0 or ny < 0 or h <= nx or w <= ny: 
                answer += 1
            
            elif arr[nx][ny] == 0:
                answer += 1


            elif arr[nx][ny] == 1 and not visited[nx][ny]:
                visited[nx][ny] = True
                que.append((nx, ny))

for i in range(h):
    for j in range(w):
        if arr[i][j] == 1 and not visited[i][j]:
            bfs(i, j)
            
print(answer)
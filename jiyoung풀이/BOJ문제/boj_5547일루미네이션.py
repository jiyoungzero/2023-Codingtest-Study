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
dxs = [[-1, 0, 1, 0, -1, -1], [0,1,1,1,0,-1]] # 홀수, 짝수
dys = [-1, -1, 0, 1, 1, 0 ]
visited = [[False for _ in range(w+2)] for _ in range(h+2)]


# 회색 = 건물 = 1
# 빈공간 = 0
def bfs(sy, sx): 
    global answer
    
    que = deque()
    que.append((sy,sx))
    visited[sy][sx] = True
    while que:
        y, x = que.popleft()

        for k in range(6):
            nx, ny = x + dxs[y%2][k], y + dys[k]
            if 0 <= ny < (h+2) and 0 <= nx < (w+2):
                if arr[ny][nx] == 1:
                    answer += 1
                else:
                    if not visited[ny][nx]:
                        visited[ny][nx] = True
                        que.append((ny, nx))
                    

    
    
bfs(0,0)
print(answer)

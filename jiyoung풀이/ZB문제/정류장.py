# 문제 설명
# 도시의 아파트에서 버스 정류장까지 거리를 구하려고 합니다.

# 도시는 격자 모양으로 지역이 구분되어 있으며, 각 지역은 아파트(1) 또는 버스 정류장(0)으로 표시합니다.

# 아파트에서 버스 정류장으로 이동은 격자를 따라서 상 하 좌 우로만 이동할 수 있으며, 대각선으로는 이동이 불가합니다. 이러한 방식으로 구하는 거리를 맨해튼 거리라고 합니다.

# hxw 크기의 도시가 2차원 정수 배열 city로 주어질 때, 각 아파트에서 가장 가까운 버스 정류장까지의 거리를 구하는 프로그램을 구현하세요.

# 결과는 입력과 동일한 크기의 2차원 정수 배열로 반환하며, 아파트 위치에는 가장 가까운 버스 정류장까지의 거리를, 버스 정류장 위치에는 0을 입력하세요.

# 단, 버스 정류장은 도시에 최소 하나 이상 존재합니다.

from collections import deque

def solution(city):
    dx, dy = [0,0,1,-1],[1,-1,0,0]
    h, w = len(city), len(city[0])
    que = deque()
    visited = [[False]*w  for _ in range(h)]
    
    for i in range(h):
        for j in range(w):
            if city[i][j] == 0:
                que.append((i, j))
                break
    
    while que:
        x, y = que.popleft()
        visited[x][y] = True
        
        for i in range(4):
            nx, ny = x+dx[i], y + dy[i]
            if 0>nx or nx >= h or 0>ny or w<=ny:continue

            if not visited[nx][ny] and city[nx][ny] == 1:
                visited[nx][ny] = True
                city[nx][ny] = city[x][y] + 1
                que.append((nx, ny))
                
    return city
                
from collections import deque

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

def bfs(N, temp, enemies, hero_x, hero_y):
    graph = [[-1] * N for _ in range(N)]  # 최단 거리 맵
    q = deque()
    for (x, y) in enemies:
        if temp[x][y] == "E":  # 기사가 아닌 적군이 있는 경우
            q.append((x, y))
            graph[x][y] = 0
    while q:  # BFS 수행
        x, y = q.popleft()
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            # 공간을 벗어난 경우 무시
            if nx < 0 or ny < 0 or nx >= N or ny >= N:
                continue
            # 벽이거나 기사가 있는 경우 무시
            if temp[nx][ny] == "X" or temp[nx][ny] == "K":
                continue
            # 처음 방문하는 경우
            if graph[nx][ny] == -1:
                graph[nx][ny] = graph[x][y] + 1  # 최단 거리 기록
                q.append((nx, ny))
    return graph

# 가만히 있는 경우 및 이동 가능한 8가지 방향
knight_dx = [0, -2, -2, -1, -1, 1, 1, 2, 2]
knight_dy = [0, -1, 1, -2, 2, -2, 2,-1, 1 ]

# 전체 보드의 크기(N)와 각 보드 정보 배열(board)을 입력받기
def solution(N, board):
    answer = 0
    temp = [[""] * N for _ in range(N)]  # 2차원 배열 생성
    hero_x = 0
    hero_y = 0
    enemies = []
    knights = []
    for i in range(N):
        for j in range(N):
            if board[i][j] == "H":
                hero_x = i
                hero_y = j
            elif board[i][j] == "E":
                enemies.append((i, j))
            elif board[i][j] == "K":
                knights.append((i, j))
    for k1 in range(9):  # 1번 기사의 이동 방향
        for k2 in range(9):  # 2번 기사의 이동 방향
            for x in range(N):
                for y in range(N):
                    temp[x][y] = board[x][y]
            # 기사는 항상 2명만 존재
            for i in range(2):
                kx, ky = knights[i]
                if i == 0:
                    nx = kx + knight_dx[k1]
                    ny = ky + knight_dy[k1]
                else:
                    nx = kx + knight_dx[k2]
                    ny = ky + knight_dy[k2]
                # 공간을 벗어난 경우 무시
                if nx < 0 or ny < 0 or nx >= N or ny >= N:
                    continue
                # 적군이 있거나 빈 공간일 때만 이동 가능
                if temp[nx][ny] == "E" or temp[nx][ny] == "B":
                    temp[kx][ky] = "B"
                    temp[nx][ny] = "K"
            graph = bfs(N, temp, enemies, hero_x, hero_y)
            if graph[hero_x][hero_y] != -1:  # 주인공에게 도달이 가능한 경우
                if answer < graph[hero_x][hero_y]:
                    answer = max(answer, graph[hero_x][hero_y])
            else:  # 주인공에게 도달이 불가능하도록 할 수 있다면
                return 0
    return answer
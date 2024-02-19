from collections import deque
import sys
input = sys.stdin.readline

n, m, fuel = map(int, input().split())
arr = [[]]
for _ in range(n):
    arr.append([0]+list(map(int, input().split())))
    
taxi = map(int, input().split())
passengers = [list(map(int, input().split())) for _ in range(m)]

dxs = [0, 1, 0, -1]
dys = [1, 0, -1, 0]

def find_person():
    tx, ty = taxi
    dist_map = get_dist(tx, ty)
    passengers.sort(key=lambda x : (-dist_map[x[0]][x[1]], -x[0], -x[1]))
    sx, sy, ex, ey = passengers.pop()
    return [sx, sy, ex, ey, dist_map[sx][sy]]

def get_dist(a, b):
    que = deque()
    que.append((a, b))
    visited = [[-1 for _ in range(n+1)] for _ in range(n+1)]
    visited[a][b] = 0
    
    while que:
        x, y = que.popleft()
        for k in range(4):
            nx, ny = x + dxs[k], y + dys[k]
            if 1 <= nx <= n and 1 <= ny <= n and visited[nx][ny] == -1:
                if arr[nx][ny] == 0:
                    visited[nx][ny] = visited[x][y] + 1
                    que.append((nx, ny))
    return visited
                

def drive():
    global taxi, fuel
    # 픽업
    sx, sy, ex, ey, dist = find_person()
    if dist == -1:
        return False
    fuel -= dist
    if fuel < 0:
        return False
    
    # 픽아웃
    used = get_dist(sx, sy)
    if used[ex][ey] == -1:
        return False
    fuel -= used[ex][ey]
    if fuel < 0:
        return False
    fuel += used[ex][ey]*2
    taxi = [ex, ey]
    return True

for _ in range(m):
    if not drive():
        fuel = -1
        break
    
print(fuel)
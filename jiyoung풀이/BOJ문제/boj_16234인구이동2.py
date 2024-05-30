import sys
input = sys.stdin.readline 
from collections import deque

N, L, R = map(int, input().split())
arr = [list(map(int, input().split())) for _ in range(N)]
answer = 0 

dxs, dys = [0,0,1,-1],[1,-1,0,0]
row, col = len(arr), len(arr[0])


def in_range(x, y):
    return 0 <= x < row and 0 <= y < col

    
while True: 
    visited = [[False]*col for _ in range(row)]
    unions = []
    
    def get_union(sx, sy): 
        que = deque()
        que.append((sx, sy))
        visited[sx][sy] = True
        result = [(sx, sy)]
        while que:
            x, y = que.popleft()
            for k in range(4):
                nx, ny = x+ dxs[k], y + dys[k]
                if not in_range(nx, ny):continue
                if visited[nx][ny] : continue
                if L <= abs(arr[x][y] - arr[nx][ny]) <= R:
                    visited[nx][ny] = True
                    result.append((nx, ny))
                    que.append((nx, ny))
        return result
                    
        
    def moving(unions):
        for union in unions:
            popul = 0
            for x, y in union:
                popul += arr[x][y]
            nxt_popul = popul//len(union)
            for x, y in union:
                arr[x][y] = nxt_popul
        return         


    for i in range(row):
        for j in range(col):
            if visited[i][j]:continue
            result = get_union(i, j)
            if len(result) > 1:
                unions.append(result) # 연합하고 있는 
    
    if len(unions) > 0:
        moving(unions) # 인구이동
        answer += 1
    else:
        break
print(answer)
from collections import deque
n, m = map(int, (input().split()))
arr = [list(map(int, input().split())) for _ in range(n)]

comb = [0]*m # 활성바이러스 조합
result = int(1e9)
virus = [] # 바이러스 위치
dx, dy = [0,0,1,-1],[1,-1,0,0]

# 바이러스 위치 담아주기
for i in range(n):
    for j in range(n):
        if arr[i][j] == 2:
            virus.append([i, j])

# 바이러스 조합 구하기
def combination(cur, cnt):
    global result
    if(cnt == m):
        result = min(result, bfs()) 
        return 
    for i in range(cur, len(virus)):
        comb[cnt] = i
        combination(i+1, cnt+1)
    
# 바이러스 퍼트리기    
def bfs():
    q = deque()
    visited = [[-1]*n for _ in range(n)]
    for idx in comb:
        q.append([virus[idx][0], virus[idx][1]])
        visited[virus[idx][0]][virus[idx][1]] = 0 # 활성바이러스 자리
        
    while q:
        x, y = q.popleft()
        for k in range(4):
            nx, ny = x+dx[k], y+dy[k]
            if nx<0 or ny <0 or n <= nx or n<= ny or visited[nx][ny] != -1:
                continue
            if arr[nx][ny] == 0 or arr[nx][ny] == 2 :
                visited[nx][ny] = visited[x][y] + 1
                q.append([nx, ny])
    
    # 퍼트린 다음에 보기
    time = 0
    for i in range(n):
        for j in range(n):
            if arr[i][j] == 0:
                # 빈칸인데 -1로, 방문하지 않았을 경우,
                if visited[i][j] == -1:
                    return -1
                else:
                    time = max(time, visited[i][j])
    return time

combination(0,0)

print(result)
        
        
    





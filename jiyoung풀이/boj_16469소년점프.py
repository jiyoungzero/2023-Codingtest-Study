# 그래프 탐색 
# 악당들을 각각 queue에 넣고 tmp_graph에 기록된 시간 총 합쳐서 각각의 위치에서의 최댓값찾기
import sys
from collections import deque
input = sys.stdin.readline

r, c = map(int, input().split())
graph = []
for _ in range(r):
    graph.append(list(map(int, input().rstrip())))
# 벽은 -1로 미리 바꾸기
for i in range(r):
    for j in range(c):
        if graph[i][j] == 1:graph[i][j] = -1
        
bads = []
for _ in range(3):
    a, b = map(int, input().split())
    bads.append((a-1, b-1))
dxs, dys = [0,0,1,-1],[1,-1,0,0]
bad_history = []

def bfs(x, y):
    queue = deque()
    queue.append((x,y))
    tmp_graph = [g[:] for g in graph]
    tmp_graph[x][y] = 0
    while queue:
        x, y = queue.popleft()
        for k in range(4):
            nx, ny = x+dxs[k], y+dys[k]
            if 0>nx or r<=nx or 0>ny or c<=ny : continue
            if graph[nx][ny] == 1:continue
            if tmp_graph[nx][ny] == 0: # 방문한적없고, 벽이 없으면 
                tmp_graph[nx][ny] = tmp_graph[x][y] + 1 # 시간 기록
                queue.append((nx, ny))
    tmp_graph[x][y] = 0   # 가만히 있는 경우 
    
    # 방문안한곳은 나중에 연산 쉽게 하기 위해서 -1
    for i in range(r):
        for j in range(c):
            if tmp_graph[i][j] == 0:tmp_graph[i][j] = -1
    return tmp_graph
    
# 악당들의 총 시간 합치기
for bad in bads:
    tmp=bfs(bad[0], bad[1])
    bad_history.append(tmp)
result = []
for i in range(r):
    for j in range(c):
        if bad_history[0][i][j] < 0 or bad_history[1][i][j] < 0 or bad_history[2][i][j] < 0:
            continue
        else:
            result.append(max(bad_history[0][i][j],bad_history[1][i][j],bad_history[2][i][j]))

# result에 아무것도 안 담기면 같은 자리에 동일하게 도달할 수 있는 경우가 없음 -> -1
if len(result) == 0:print(-1)
else:
    result.sort()
    cnt = 0
    ans = result[0]
    for ele in result:
        if ele != ans:break
        cnt += 1
    print(ans)
    print(cnt)
    
    


from collections import deque
import sys
input = sys.stdin.readline

n, m, v = map(int, input().split())
graph = [[0]*(n+1) for _ in range(n+1)]

# 스택을 reverse()로 출력하는 거 --> stack[::-1]
# # 서로 관련 있는 거 찾아서 매칭 == 1 
for _ in range(m):
    a,b = map(int, input().split())
    graph[a][b] = graph[b][a] = 1

visited1 = [0] * (n+1)
visited2 = [0] * (n+1)

def dfs(v): # 재귀의 성질을 띄어요! 
    visited1[v] = 1 
    print(v, end=" ")
    for i in range(n+1):
        if visited1[i] == 0 and graph[v][i] ==1:
            dfs(i)
def bfs(v): # 큐의 성질을 띄어요! 
    q = deque()
    q.append(v)
    visited2[v] = 1  # 맨 처음 시작 할 때는 while 문내에서 하면 중복(상관없긴 한데)되어서 밖에서 해주는게 깔끔 
    while q:
        v = q.popleft()
        print(v, end =" ")
              
        for i in range(n+1):
            if visited2[i] == 0 and graph[v][i] == 1:
                q.append(i)
                visited2[i] = 1

dfs(v)
print()
bfs(v) 
    
    

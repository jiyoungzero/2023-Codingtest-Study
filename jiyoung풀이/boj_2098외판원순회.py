# 비트마스킹(&, |, ^, ~, >>, <<), dp, dfs?
# dp[cur][vist] = dp[next][nextvisit] + graph[cur][next] 
#  dp[cur][visit] : 방문현황, 아직 방문못한 도시를 모두 거쳐서 순회하는데 필요한 최소 비용
#  dp[0][0011(2)] = dp[2][0111(2)] + graph[2][0]


import sys
input = sys.stdin.readline
INF = int(1e9)

n = int(input())
graph = []
dp = [[INF]*(1<<n) for _ in range(n)] # 1<<4(1*2^4) == 10000(2)
dxs, dys = [0,0,1,-1], [1,-1,0,0]
# visited = [[False]*n for _ in range(n)]

for i in range(n):
    graph.append(list(map(int, input().split())))

def dfs(x, visited):
    if visited == (1<<n) -1 : # 모든 도시 다 방문했을때 1111(2)
        if graph[x][0]:# 시작점(임의로 0)으로 되돌아갈 길이 있을 때, 없을때
            return graph[x][0] 
        else:return INF
    
    
    if dp[x][visited] != INF:# 이미 최소비용이면 통과
        return dp[x][visited]
    
    for i in range(1,n):
        if (not graph[x][i]) or (visited & (1<<i)):# 가는 경로가 없거나, 방문했으면 통과
            continue
        dp[x][visited] = min(dp[x][visited], dfs(i, visited|(1<<i)) + graph[x][i]) # 그 외에는 dp로 최소비용 업데이트 (아직 안간 도시들은 |, dfs로 계산)
    return dp[x][visited]

print(dfs(0, 1)) # visited = 1이면 0001(2) == 0번도시는 시작하면서 방문함
            
            
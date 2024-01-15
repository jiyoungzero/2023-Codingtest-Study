
# 다익스트라 : 최단 경로 + cost 
import heapq
INF = int(1e9)

dxs, dys = [0,0,1,-1], [1,-1,0,0]
def solution(N, arr):
    answer = 0
    cost = [[INF]*N for _ in range(N)]
    graph = [[None]*N for _ in range(N)]
    
    def in_range(x, y):
        return 0 <= x < N and 0 <= y < N
    
    for i in range(N):
        for j in range(N):
            graph[i][j] = [] # 초기화
            for k in range(4):
                ni, nj = i + dxs[k], j + dys[k]
                if not in_range(ni, nj):
                    continue
                diff = abs(arr[i][j] - arr[ni][nj])
                graph[i][j].append((ni, nj, diff))
    
    def dijkstra(s_x, s_y):
        heap = []
        heapq.heappush(heap, (0, s_x, s_y))
        cost[s_x][s_y] = 0
        
        while heap:
            diff, cur_x, cur_y = heapq.heappop(heap)
            if cost[cur_x][cur_y] < diff:
                continue
            for (nx, ny, n_diff) in graph[cur_x][cur_y]:
                nxt_cost =  diff + n_diff 
                if nxt_cost < cost[nx][ny]:
                    cost[nx][ny] = nxt_cost
                    heapq.heappush(heap, (nxt_cost, nx, ny))
    dijkstra(0,0)
                
    answer = cost[N-1][N-1]
    
    return answer


print(solution(5, [[0, 0, 0, 0, 1],[1, 1, 1, 0, 1],[1, 4, 4, 4, 4],[1, 1, 4, 3, 3],[0, 1, 3, 1, 1]]))

print(solution(6, [[0, 5, 6, 2, 3, 8],[1, 1, 1, 1, 1, 1],[5, 6, 5, 3, 2, 3],[2, 6, 5, 2, 2, 4],[7, 7, 7, 3, 5, 6],[6, 7, 8, 4, 4, 3]]
))
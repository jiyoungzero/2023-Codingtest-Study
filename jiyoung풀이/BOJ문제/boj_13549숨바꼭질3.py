import sys
input = sys.stdin.readline 
import heapq

n, k = map(int, input().split())
moves = [2, -1, 1]
answer = int(1e9)


que = []
visited = [False]*100001
visited[n] = True
heapq.heappush(que, (0,n))

while que:
    time, x  = heapq.heappop(que)
    # print(que)
    
    if x == k:
        answer = min(answer, time)
        break
    
    for dir in moves:
        if dir == 2:
            nx = x*2
            n_time = time
        else:
            nx = x + dir
            n_time = time + 1
        if 0 <= nx < 100001:
            if not visited[nx]:
                heapq.heappush(que, (n_time, nx))
                visited[nx] = True

        
print(answer)



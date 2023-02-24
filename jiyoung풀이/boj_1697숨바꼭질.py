# 그래프탐색

import sys
input =sys.stdin.readline
from collections import deque
INF = int(1e9)
n, k = map(int, input().split())
time = [INF] * (100001)

def bfs(start_x):
    que = deque([start_x])
    time[start_x] = 0
    while que:
        x = que.popleft()
        if x == k:break
        
        # 아래는 시간초과 뜸
        # if 0<=(x-1)<100001 and time[x-1] == INF  :
        #     time[x-1] = time[x] + 1
        #     que.append(x-1)
        # if   0<=(x+1)<100001 and time[x+1] == INF:
        #     time[x-1] = time[x] + 1
        #     que.append(x+1)
        # if 0<=(x*2)<100001  and time[x*2] == INF:
        #     time[x*2] = time[x] + 1
        #     que.append(x*2)
        
        # 중요 > 인덱스 검사를 먼저 해놓기 그래야 인덱스 에러가 안남 
        for i in (x-1, x+1, x*2):
            if 0<=i<100001 and time[i] == INF:
                time[i] = time[x] + 1
                que.append(i)

bfs(n)
print(time[k])     
    

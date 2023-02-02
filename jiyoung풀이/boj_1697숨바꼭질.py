# 그래프탐색

import sys
input = sys.stdin.readline
import heapq
from collections import deque
INF = int(1e9)

n, k = map(int, input().split())
start = n
distance = [INF] * (100001)

distance[start] = 0
q = deque([start])
while q:
    now = q.popleft()
    if now == k:break

    for i in (now-1, now+1, 2*now):
        if 0<=i<100001 and distance[i] == INF:
            distance[i] = distance[now] + 1
            q.append(i)
     
print(distance[k])

# 최소힙
# 실버 2

import heapq
import sys
input = sys.stdin.readline # 필수

arr = []
result = []
heapq.heapify(arr)
N = int(input())
for _ in range(N):
    x = float(input())
    if x == 0:
        if not arr:
            print(0)
            continue
        print(int(heapq.heappop(arr)))
        continue
    if x == int(x):
        heapq.heappush(arr, x)

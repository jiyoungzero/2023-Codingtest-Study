import sys
input = sys.stdin.readline 
import heapq

n, k = map(int, input().split())
jewels = [tuple(map(int, input().split())) for _ in range(n)] # weight, value
bags = [int(input()) for _ in range(k)]
answer = 0
heap = []
jewels.sort(key =lambda x: (-x[0]))
bags.sort()
for bag in bags: 
    while jewels: # 가벼운 보석 순으로 나옴 
        weight, value = jewels.pop()
        if bag < weight:
            jewels.append((weight, value))
            break
        else:
            heapq.heappush(heap, -value)
    print(jewels, heap)
    if heap:
        # print(heapq.heappop(heap))
        answer -= heapq.heappop(heap)
print(answer)




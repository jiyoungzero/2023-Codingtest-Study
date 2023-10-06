import heapq
def solution(jobs):
    answer = 0
    now_time, i = 0,0
    start = -1
    heap = []
    
    while i < len(jobs):
        for j in jobs:
            if start < j[0] <= now_time:
                heapq.heappush(heap, [j[1], j[0]])
            
        if len(heap) > 0:
            cur = heapq.heappop(heap)

            start = now_time
            now_time += cur[0]

            answer += (now_time-cur[1])
            i += 1
        else:
            now_time += 1
    
    return answer//len(jobs)
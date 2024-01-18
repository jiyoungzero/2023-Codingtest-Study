# 그리디

# 매개변수 형식
# activity = {{0, 5}, {2, 6}, {3, 5}, {7, 10}, {5, 9}, {13, 15}}

# 반환값 형식
# 3


import heapq 
def solution(activity):
    activity.sort()
    cnt = 1
    heap = [activity[0][1]]
    
    for act in activity[1:]:
        start, end = act
        if start > heap[0]:
            heapq.heappop(heap)
            heapq.heappush(end)
        else:
            cnt += 1
            heapq.heappush(heap, end)
    return cnt
            
import heapq

def solution(food_times, k):
    answer = -1
    hq = []
    for i in range(len(food_times)):
        heapq.heappush(hq, (food_times[i], i+1)) # 섭취시간, 순번
    
    prev_time = 0
    length = len(food_times)
    
    while hq:
        now = (hq[0][0] - prev_time)*length
        if now <= k:
            k -= now
            length -= 1
            prev_time, _ = heapq.heappop(hq)
        else:
            idx = k % length
            hq.sort(key=lambda x:x[1])
            answer = hq[idx][1]
            break
            

    
    return answer
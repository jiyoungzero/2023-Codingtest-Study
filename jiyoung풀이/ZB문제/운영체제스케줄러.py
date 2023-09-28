from heapq import heappush, heappop
def solution(start, time):
    answer = [0 for _ in range(len(start))]
    jobs = []

    for i, (s, t) in enumerate(zip(start, time)):
        jobs.append((s, t, i))
    jobs.sort(key=lambda x:(x[0], x[2]))

    heap = []
    idx, t = 0,0

    while idx < len(answer):
        while jobs and t >= jobs[0][0]:
            s_, t_, i_ = jobs[0]
            heappush(heap, (t_, i_, s_))
            heappop(heap)
        
        if len(heap) != 0:
            now = heap[0]
            t += now[0]
            answer[idx] = now[1]
            idx += 1
        else:# 처음
            t = jobs[0][0]
            while jobs and t >= jobs[0][0]:
                s_, t_, i_ = jobs[0]
                heappush(heap, (t_, i_, s_))
                heappop(heap)
    return answer
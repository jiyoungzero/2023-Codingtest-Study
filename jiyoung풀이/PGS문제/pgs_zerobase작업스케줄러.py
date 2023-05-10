# 매개변수 형식
# start = {0, 2, 3, 5, 6}
# time = {2, 4, 2, 1, 3}

# 반환값 형식
# {0, 1, 3, 2, 4}

import heapq

def solution(start, time):
    answer = []
    n = len(start)
    tasks = sorted(zip(start, time))
    print(tasks)
    heap = []
    cur_time = tasks[0][0]
    i = 0
    
    while heap or i < n:
        if heap:
            t, s, idx = heapq.heappop(heap)
            cur_time += t
            answer.append(idx)
        else:
            cur_time = tasks[i][0]
        
        while i<n and tasks[i][0] <= cur_time:
            s, t = tasks[i]
            heapq.heappush(heap, (t,s, i))
            i += 1
    return answer

# start = {0, 2, 3, 5, 6}
# time = {2, 4, 2, 1, 3}
print(solution([0, 2, 3, 5, 6],[2, 4, 2, 1, 3]))

# 모범답안
from queue import PriorityQueue

def solution(start, time):
    tasks = [(st[0], st[1], i)
            for i, st in enumerate(zip(start, time))]
    
    tasks.sort(key=lambda x: (x[0], x[2]))
    
    pq = PriorityQueue()
    answer = [0 for _ in range(len(tasks))]
    idx = 0
    time = 0
    while idx < len(answer):
        while tasks and time >= tasks[0][0]:
            start_, time_, idx_ = tasks[0]
            pq.put((time_, idx_, start_))
            del tasks[0]

        if not pq.empty():
            current_task = pq.get()
            time += current_task[0]
            answer[idx] = current_task[1]
            idx += 1
        else:
            time = tasks[0][0]
            while tasks and time >= tasks[0][0]:
                start_, time_, idx_ = tasks[0]
                pq.put((time_, idx_, start_))
                del tasks[0]
    return answer
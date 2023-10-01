# 
from collections import deque
def solution(plans):
    answer = []
    que = deque()
    jobs = []
    
    for p in plans: 
        name, start, time = p[0], int(p[1][:2])*60+int(p[1][3:]), int(p[2])
        jobs.append((name, start, time))
        
    jobs.sort(key = lambda x : x[1])
    print(jobs)
    
    return answer
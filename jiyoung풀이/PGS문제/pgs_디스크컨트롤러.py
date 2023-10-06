def solution(jobs):
    answer = 0
    jobs.sort(key=lambda x:x[1])
    
    now_time = jobs[0][0]+jobs[0][1]
    total = jobs[0][0]+jobs[0][1]
    for i in range(1, len(jobs)):
        if now_time > jobs[i][0]:
            total += ((now_time-jobs[i][0])+jobs[i][1])
        else:
            total += t
        now_time += jobs[i][1]
            
    return total // len(jobs)
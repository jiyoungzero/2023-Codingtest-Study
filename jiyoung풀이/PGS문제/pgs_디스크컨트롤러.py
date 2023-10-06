def solution(jobs):
    answer = 0
    n = len(jobs)
    jobs.sort(key=lambda x:x[0])
    now_time = jobs[0][0]+jobs[0][1]
    total = jobs[0][0]+jobs[0][1]
    del jobs[0]
    
    while jobs:
        disk = []
        for i in range(len(jobs)):
            if now_time >= jobs[i][0]:
                disk.append(jobs[i])
        if len(disk) == 0:
            total += (jobs[0][0] + jobs[0][1])
            now_time = jobs[0][0] + jobs[0][1]
            del jobs[0]
            
        else:
            disk.sort(key=lambda x:x[1])
            total += ((now_time-disk[0][0])+disk[0][1])
            now_time += disk[0][1]
            for i, (s, t) in enumerate(jobs):
                if [s,t] == disk[0]:
                    del jobs[i]

    
            
    return total // n
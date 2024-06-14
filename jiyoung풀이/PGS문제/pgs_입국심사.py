def solution(n, times):
    max_time = max(times)*n
    answer = max_time
    
    s, e = 0, max_time
    while s <= e:
        mid = (s+e)//2
        # print(mid)
        
        cnt = 0
        for time in times:
            cnt += (mid)//time
        
        if cnt >= n:
            answer = min(answer, mid)
            e = mid - 1
        else:
            s = mid + 1
        
        
    return answer
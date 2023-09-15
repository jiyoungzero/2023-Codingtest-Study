def solution(delay, capacity, times):
    answer = 0
    message_cnt = 0
    time_cnt = 0
    
    for i in times:
        time_cnt += 1
        if time_cnt >= delay:
            message_cnt -=(time_cnt//delay)
            time_cnt %= delay
        
        message_cnt += 1
        if message_cnt >= capacity:
            message_cnt -= 1
            answer += 1
    return answer
             
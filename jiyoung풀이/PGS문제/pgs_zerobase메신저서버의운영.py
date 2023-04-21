def solution(delay, capacity, times):
    current_time = 0
    current_que = 0
    result = 0
    
    for time in times:
        current_time += time
        sent = current_time // delay
        current_que = max(0, current_que - sent)
        if current_que == capacity:
            result += 1
        else:
            current_que += 1
        
        current_que %= delay
    return result
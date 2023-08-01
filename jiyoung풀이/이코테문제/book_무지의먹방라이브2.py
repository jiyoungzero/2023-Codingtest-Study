# 정확성도 틀림.
def solution(food_times, k):
    answer = 0
    now = 0
    
    while 1:
        now = (now + 1)%len(food_times)
        if k == 0:
            answer = now
            break
        if food_times[now] > 0:
            food_times[now] -= 1
            k -= 1
        elif food_times[now] == 0:
            continue
    
    return answer
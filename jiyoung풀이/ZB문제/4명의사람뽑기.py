def solution(names):
    answer = 1
    names = list(set(names))
    n = len(names)
    cnt = 0

    while cnt != 4:
        answer *= n
        n -= 1
        cnt += 1
    
    for i in range(1,5):
        answer //= i
 
    return answer
def solution(delay, N):
    answer = 1
    que = []
    que.append(0) # 시간
    
    for _ in range(N):
        temp = []
        while que:
            t = que.pop(0)
            if t == 0:
                temp.append(0)
                temp.append(delay)
                answer += 2
            else:
                temp.append(t-1)
        que = temp
    return answer
# 40점
from collections import deque
def solution(priorities, location):
    answer = []
    if len(priorities)==1:return 1
    
    que = deque()
    for i in range(len(priorities)):
        now = priorities[i]
        if i+1 < len(priorities) and max(priorities[i+1:]) > now:
            que.append((now, i)) # 현재 값, 인덱스
        else:answer.append((now, i))
                
    answer += list(que)
    for idx, ele in enumerate(answer):
        if ele[1] == location:
            answer = idx+1
            
    return answer


# any라는 함수를 처음 알게 되었다. all이라는 함수도 있음!
def solution(priorities, location):
    answer = 0
    que = [(i, v) for i, v in enumerate(priorities)]

    while 1:
        cur = que.pop(0)
        if any(cur[1] < q[1] for q in que):
            que.append(cur)
        else:
            answer += 1
            if cur[0] == location:return answer


    return answer
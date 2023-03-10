# 25점
from collections import deque
def solution(priorities, location):
    answer = []
    
    que = deque()
    for i in range(len(priorities)):
        now = priorities[i]
        if i+1 < len(priorities) and max(priorities[i+1:]) > now:
            que.append((now, i)) # 현재 값, 인덱스
        else:
            if que:
                answer.append((now, i))
                
    print(answer, que)
    answer += list(que)
    for idx, ele in enumerate(answer):
        if ele[1] == location:
            answer = idx+1
            
    return answer
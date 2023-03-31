# 2022 카카오 tech internship

# 이거 처음에 감 못잡음 (0/3)

# 그리디넹
from collections import deque
def solution(queue1, queue2):
    que1 = deque(queue1)
    que2 = deque(queue2)
    sum1 = sum(que1)
    sum2 = sum(que2)
    answer = 0
    max_cnt = len(que1) * 4
    
    if (sum1 + sum2)%2 != 0:return -1
    
    while 1:
        if sum1 > sum2:
            tmp = que1.popleft()
            que2.append(tmp)
            sum1 -= tmp
            sum2 += tmp
            answer += 1
        elif sum1 < sum2:
            tmp = que2.popleft()
            que1.append(tmp)
            sum1 += tmp
            sum2 -= tmp
            answer += 1
        else:break
        
        if answer == max_cnt:
            answer = -1
            break
    
    return answer
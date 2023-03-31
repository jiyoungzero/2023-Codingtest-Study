# 2022 카카오 tech internship

# 이거 처음에 감 못잡음 (0/3)

# 백트래킹?
from copy import deepcopy
answer = int(1e9)
def solution(que1, que2):
    # answer = -2
    global answer
    target = sum(que1) + sum(que2) / 2
    answer = backtracking(que1, que2, target,0)
    
    return answer

def backtracking(q1, q2, target, cnt):
    global answer
    if sum(q1) == target:
        answer = min(answer, cnt)
        print("ss")
        return 
    else:
        tmp1 = deepcopy(q1)
        tmp2 = deepcopy(q2)
        if sum(tmp1) > sum(tmp2):
            value = tmp1.popleft()
            tmp2.append(value)
            backtracking(tmp1, tmp2, target, cnt+1)
            tmp1.append(value)
            tmp2.pop()
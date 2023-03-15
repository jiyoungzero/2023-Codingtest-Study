# 완탐 

# 시간초과(런타임에러)

def solution(answers):
    answer = []
    one = [1,2,3,4,5]
    two = [2,1,2,3,2,4,2,5]
    three = [3,3,1,1,2,2,4,4,5,5]
    t = [0 ,0 ,0]
    
    for i, ele in enumerate(answers):
        if ele == one[i]:
            t[0] += 1
        if ele == two[i]:
            t[1] += 1
        if ele == three[i]:
            t[2] += 1
    max_answer = max(t)
    
    for i, ele in enumerate(t):
        if ele == max_answer:
            answer.append(i+1)
    
    return answer
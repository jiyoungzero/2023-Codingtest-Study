# 완탐 

def solution(answers):
    answer = []
    tmp = [0,0,0]
    one = [1,2,3,4,5]
    two = [2, 1, 2, 3, 2, 4, 2, 5]
    three = [3, 3, 1, 1, 2, 2, 4, 4, 5, 5]

    for i, ele in enumerate(answers):
        if one[i%5] == ele:
            tmp[0] += 1
        if two[i%8] == ele:
            tmp[1] += 1
        if three[i%10] == ele:
            tmp[2] += 1
    
    max_answer = max(tmp)
    for i, ele in enumerate(tmp):
        if ele == max_answer:
            answer.append(i+1)
    
    return answer
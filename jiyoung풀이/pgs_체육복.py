# 그리디 

# 시간초과
def solution(n, lost, reserve):
    answer = n-len(lost)

    for ele in lost:
        if ele == 1 or ele == n:
            if 2 in reserve:
                answer += 1 
                reserve.remove(2)
            elif n in reserve:
                answer += 1
                reserve.remove(n-1)
        elif (ele-1) in reserve :
                answer += 1
                reserve.remove(ele-1)
        elif (ele+1) in reserve:
                answer += 1
                reserve.remove(ele+1)


    return answer
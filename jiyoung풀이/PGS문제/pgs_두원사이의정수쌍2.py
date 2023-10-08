# 포인트는 x축을 기준으로 count하는 것..
import math
def solution(r1, r2):
    answer = 0
    max_, min_ = 0,0
    for i in range(1,r2+1):
        max_ = int(math.sqrt(r2**2-i**2))
        if r1 > i:
            min_ = math.ceil(math.sqrt(r1**2-i**2))
        else:
            min_ = 0
        answer += (max_-min_+1)



    return answer*4
# 구현
import sys
input = sys.stdin.readline
from math import comb, perm
from functools import reduce

def solution(N,M,K,capacity):
    sum_capacity = sum(capacity)
    answer = 1
    if sum_capacity == N:
        for k in capacity:
            answer *= comb(N,k)
        answer *= perm(K, M)
        return answer
    else:
        # 학생 배정하기 
        student_case = 0
        capacity_multi = reduce(lambda x,y:x*(y+1), capacity, 1)
        for i in range(capacity_multi):
            # [5,3,4]
            caps = [0 for _ in range(M)]
            den = capacity_multi
            num = i
            for j in range(caps):
                den = den // capacity[j] + 1
                caps[j] = num // den
                num %= den
            if sum(caps) == N:
                student_left = N
                current_class = 1
                for cap in caps:
                    current_class *= comb(student_left, cap)
                    student_left -= cap
        return student_left*perm(K,M)
                

        
    
print(solution(10,3,4,[3,3,4]))
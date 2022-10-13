# 문제 스스로 풀어보기

# 평균 값을 보고 그 원소값들을 구하는 문제 --> 평균의 성질만 이용하면 끝
# 10분 소요 

import sys
input = sys.stdin.readline

n = int(input())
avg_lst = list(map(int, input().split()))
lst = [avg_lst[0]]

for i in range(1, n):
    sum_value = avg_lst[i]*(i+1)
    lst.append(sum_value - sum(lst[:i]))

for ele in lst:
    print(ele, end=" ")
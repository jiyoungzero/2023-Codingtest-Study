# 문제 스스로 풀어보기

import sys
input = sys.stdin.readline

T =int(input())

for test_case in range(1,T+1):
    result = 0
     
    lst = list(input().rstrip())
    r_lst = []
    for i in range(len(lst)-1, -1, -1):
        r_lst.append(lst[i])
    print(lst, r_lst)
    if lst == r_lst:
        result = 1
    print(f"#{test_case} {result}")
# 문제 스스로 풀어보기 

import sys
input = sys.stdin.readline

test_case = int(input())

for T in range(1, test_case+1):
    result = 0
    lst = list(map(int, input().split()))
    
    result = sum(lst)/len(lst)
    if result%1 >= 0.5:
        result = sum(lst) // len(lst) + 1
    else:
        result = sum(lst) // len(lst)
    
    print(f"#{T} {result}")
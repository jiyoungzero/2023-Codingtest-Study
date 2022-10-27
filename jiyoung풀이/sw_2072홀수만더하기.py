# 문제 스스로 풀어보기 

import sys
input = sys.stdin.readline

test_case = int(input())
for _ in range(test_case):
    arr = list(map(int, input().split()))
    result = 0
    for ele in arr :
        if ele % 2 != 0:
            result += ele
    print(result)




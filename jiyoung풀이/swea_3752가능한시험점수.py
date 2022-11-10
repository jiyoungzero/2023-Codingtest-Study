# 문제 스스로 풀어보기

import sys
input = sys.stdin.readline
import itertools

T = int(input().rstrip())

for t in range(1, T+1):
    result = set()
    
    n = int(input())
    prob = list(map(int, input().split()))
    
    # for i in range(n):
    #     for j in range(i, n):
    #         if sum(prob[i:j]) not in result:
    #             result.add(sum(prob[i:j]))
    for i in range(n+1):
        c_prob = itertools.combinations(prob, i)
        for c in list(c_prob):
            result.add(sum(c))

    print(result)
    print(f"#{t} {len(result)}")
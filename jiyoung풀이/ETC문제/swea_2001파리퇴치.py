# 문제 스스로 풀어보기
# N의 크기가 작기 때문에 완탐으로 풀 수 있을 것 같다

import sys
input = sys.stdin.readline

T = int(input())

for test_case in range(1, T+1):
    result, max_value = 0, 0
    N, M = map(int, input().split())

    arr = [list(map(int, input().split())) for _ in range(N)]
    
    for i in range(N-M+1):
        for j in range(N-M+1):
            max_value = 0
            for a in range(M):
                for b in range(M):
                    max_value += arr[i+a][j+b]
            
            
                result = max(result, max_value)
    
    print(f"#{test_case} {result}")
    
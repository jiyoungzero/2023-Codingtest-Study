# 문제 스스로 풀어보기

import sys
input = sys.stdin.readline

test_case = int(input())

for T in range(1,test_case+1):
    n = int(input().rstrip())
    lst = list(map(int, input().split()))
    result = 0
    # 양 옆을 탐색 (lst[i-2], lst[i+2])해서 제일 큰 수보다 위에 있는 칸 수를 센다
    for i in range(2,n-2):
        l = max(lst[i-2:i])
        r = max(lst[i+1:i+3])
        if max(l,r) < lst[i]:
            result += (lst[i] - max(l,r))

        else:
            continue
            
    print(f"#{T} {result}")

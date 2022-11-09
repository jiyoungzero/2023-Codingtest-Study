# 문제 스스로 풀어보기

# the candy war과 비슷하다고 느낌 

import sys
input = sys.stdin.readline

# capcity, amount
lst = []
for _ in range(3):
    c, a = map(int, input().split())
    lst.append([c,a])

for i in range(100):
    if lst[i%3][1] + lst[(i+1)%3][1] <= lst[(i+1)%3][0]:
        lst[(i+1)%3][1] += lst[i%3][1]
        lst[i%3][1] = 0
    else:
        # 다음 양동이의 양과 현재 양동이의 양을 더한 값이, 다음양동이의 용량을 초과하면
        temp = lst[(i+1)%3][0] - lst[(i+1)%3][1]
        lst[(i+1)%3][1] += temp
        lst[i%3][1] -= temp

for i in range(3):
    print(lst[i][1])


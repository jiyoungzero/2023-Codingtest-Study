# 자료구조, 스택, 시뮬레이션
# 하, 20분

import sys
input = sys.stdin.readline  # 꼭하기

k = int(input())
result = []
for _ in range(k):
    num = int(input())
    if num == 0:
        if result:
            result.pop()
        else:
            continue
    else:
        result.append(num)
print(sum(result))

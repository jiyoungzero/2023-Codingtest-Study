# 자료구조, 덱
# 하, 30분
# 꼭 deque으로 풀어야 하는가?

# 틀림 -> why?
from collections import deque
import sys
input = sys.stdin.readline

n, k = map(int, input().split())
d = deque([i for i in range(1, n+1)])
result = []

for i in range(n):  # len(queue) -> 큐 요소가 빠져나가기 때문에?? 확인해보기
    for j in range(k-1):
        d.append(d.popleft())
    result.append(d.popleft())

print('<', end='')
for i in range(len(result)):
    if i < len(result) - 1:
        print(result[i], end=', ')
    else:  # 마지막 원소
        print(result[i], end='')
print('>', end='')

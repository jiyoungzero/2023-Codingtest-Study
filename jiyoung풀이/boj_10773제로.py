# 문제 스스로 풀어보기

# 스택 : pop을 0일때 실행
# 

import sys
input = sys.stdin.readline

n = int(input())
result = 0
stack = []

for _ in range(n):
    value = int(input())
    if value == 0 and len(stack) != 0:
        stack.pop()
    else:
        stack.append(value)
        
print(sum(stack))
        

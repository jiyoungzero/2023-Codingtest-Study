# 문제 스스로 풀어보기

# 스택 문제, append, pop
# 오름차순으로 push, 불가능하면 NO
# 30 분 초과 --> 실패 
import sys
input = sys.stdin.readline

# n = int(input())
# stack = [int(input()) for _ in range(n)]
# lst = []

# for i in range(n):


# 정답 코드
n = int(input())
stack, result = [], []
cnt = 1

for i in range(n):
    data = int(input())
    while cnt <= data:
        stack.append(cnt)
        cnt += 1
        result.append('+')
    if stack[-1] == data:
        stack.pop()
        result.append('-')
    else:
        print("NO")
        exit(0)
        
print('\n'.join(result)) # 줄바꿈을 기준으로 result 문자열을 합친다. 

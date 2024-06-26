# 실버2
# 15분 소요

import sys
from collections import deque
input = sys.stdin.readline
test_case = int(input())

for _ in range(test_case):
    L = deque(input().rstrip())
    left, right = [], []
    while L:
        data = L.popleft()
        if data == "<":
            if left:
                right.append(left.pop())
        elif data == ">":
            if right:
                left.append(right.pop())
        elif data == "-":
            if left:
                left.pop()
        else:
            left.append(data)
    while right:
        left.append(right.pop())
    print("".join(left))


'''
# 스택, 구현, 그리디
# 중, 40분

# 런타임 에러 발생.. why?
# stack 2개 두고 '<'일 경우 stack1에서 pop & stack2에 push
# '>'일 경우 stack2에서 pop & stack1에 push
# '-'일 경우 stack1에 pop & remove

test = int(input())

for _ in range(test):
    arr = list(map(str, input()))
    stack1 = []
    stack2 = []
    for i in arr:
        if i == '<':
            if stack1:
                stack2.append(stack1.pop())
        elif i == '>':
            if stack2:
                stack1.append(stack2.pop())
        elif i == '-':
            if stack1:  # 이부분을 안넣어서 런타임 에러
                stack1.pop()
        else:
            stack1.append(i)
    stack1.extend(reversed(stack2))
    print(''.join(stack1))

# 정답
# O(n) 선형시간 안에 풀어야함
# 커서를 기준으로 왼쪽, 오른쪽 stack을 둠
# 아이디어는 같은 듯
test_case = int(input())

for _ in range(test_case):
    left_stack, right_stack = [], []
    data = input()
    for i in data:
        if i == "-":
            if left_stack:
                left_stack.pop()
        elif i == ">":
            if right_stack:
                left_stack.append(right_stack.pop())
        elif i == "<":
            if left_stack:
                right_stack.append(left_stack.pop())
        else:
            left_stack.append(i)
    left_stack.extend(reversed(right_stack))
    print("".join(left_stack))

'''

# 문제 스스로 풀어보기
# 4분 소요 
import sys
input = sys.stdin.readline

n = int(input())
stack = []

for _ in range(n):
    command = input().split()
    
    if command[0] == "push":
        stack.append(command[1])
    elif command[0] == "top":
        if len(stack) != 0: 
            print(stack[-1])
        else: print(-1)
    elif command[0] == "size":
            print(len(stack))
    elif command[0] == "pop":
        if len(stack) == 0:
            print(-1)
        else :
            print(stack.pop())
    elif command[0] == "empty": 
        if len(stack) == 0 : print(1)
        else : print(0)

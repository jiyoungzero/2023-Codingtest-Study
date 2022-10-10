# 문제 스스로 풀어보기

# 스택 문제같음 -나오면 pop, < >나오면 이동(pop 했다가 push?)
# 30분 초과
import sys
input = sys.stdin.readline

# t = int(input())
# result = []

# for _ in range(t):
    
    
    
# 정답 코드
# 아이디어 : 스택을 두개 이용, 두개를 잇는 곳을 커서로 보자
#           < > 나오면 두 스택 사이로 문자열을 이동시킨다. 

test_case = int(input())

for _ in range(test_case):
    left_stack, right_stack = [], []
    data = input()
    for i in data:
        if i == "-":
            if left_stack: # 비어있지 않다면 
                left_stack.pop() # pop(0)는 가장 앞쪽 빼기 --> 큐, pop()는 가장 뒤쪽 빼기 --> 스택 
        elif i == ">":
            if right_stack:
                left_stack.append(right_stack.pop())  
        elif i == "<":
            if left_stack:
                right_stack.append(left_stack.pop())
        else:
            left_stack.append(i)        
    left_stack.extend(reversed(right_stack)) # 리스트와 리스트를 합칠때는 append가 아니라 extend이다. 
    print("".join(left_stack))      
        

   
        
    
    

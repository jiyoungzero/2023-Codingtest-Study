# 큐 
import sys
from collections import deque
input = sys.stdin.readline

test_case = int(input())


# 시간초과      
# 구현 + 뒤집기 아이디어 추가 R 이 홀수 일때만 

# for _ in range(test_case):
#     flag = True
#     p = input().rstrip()
#     n = int(input())
#     case = input()
#     tmp = case[1:-2]
#     tmp = tmp.split(",")
#     arr = []
#     if len(tmp) > 2:
#         for ele in tmp:
#             arr.append(int(ele))

#     cnt = 0 # 뒤집기 횟수
#     for command in p:
#         if command == "R":
#             cnt += 1
        
#         elif command == "D":
#             if cnt%2 != 0:
#                 arr = arr[::-1]
#                 cnt = 0
#             if arr:
#                 del arr[0]                
#             elif not arr:
#                 print("error")
#                 flag = False
#                 break
#     if flag:print(arr)
            
# deque 이용하기 

for _ in range(test_case):
    p = input().rstrip()
    n = int(input())
    arr = input().rstrip()[1:-1].split(',')
    
    queue = deque(arr)
    flag = True
    
    # 예외처리
    if n == 0:
        queue = []

    cnt = 0
    for i in p:
        if i == "R": cnt += 1
        elif i == "D":
            if len(queue) < 1:
                flag = False
                print("error")
                break
            else:
                if cnt%2 != 0:
                    queue.pop() # 뒤집고 하나 빼기
                else:
                    queue.popleft()
                    
    if flag:
        if cnt%2 == 1:
            queue.reverse()
            print("["+",".join(queue)+"]")
        else:
            print("["+",".join(queue)+"]")
# 문제 스스로 풀어보기
# 
# 회전큐를 사용하는게 좋을 것 같다
# 30분 초과

import sys
# from collections import deque
input = sys.stdin.readline

# result = []
# # 오른쪽 회전 --> que.pop() , que().appendleft()
# for _ in range(test_case):
#     n = int(input())
#     cnt = 0
    
#     que = deque(list(map(int, input().split())))
#     flag = True
    
#     while flag :
        
#         temp = 0
        
#         for i in range(n):
#             candy = que.pop()
#             if candy % 2 != 0:
#                 candy += 1
#                 que[-1] -= (candy//2)
#                 que.appendleft(candy//2+ que[0]) 
#             else: que.appendleft(candy//2+ que[0])
            
#         print(*que, sep=", ")
#         # 사탕의 개수가 모두 같은지 검사
#         if len(set(que)) == 1: flag = False
#         else: 
#             flag = True
#             cnt += 1
    
#     result.append(cnt)
        
# print(*result, sep="\n")

# 정답코드 
def check(n, candy):
    for idx in range(n):
        if candy[idx] % 2 :
            candy[idx] += 1
    return len(set(candy)) == 1

def teacher(n, candy):
    tmp_lst = [0 for i in range(n)]
    for idx in range(n):
        if candy[idx] % 2 :
            candy[idx] += 1
        candy[idx] //= 2
        
        tmp_lst[(idx+1) % n] = candy[idx]
        
    for idx in range(n):
        candy[idx] += tmp_lst[idx]
    return candy

def process():
    n = int(input())
    candy = list(map(int, input().split()))
    cnt = 0
    while not check(n, candy):
        cnt += 1
        candy = teacher(n, candy)
    print(cnt)
    
for i in range(int(input())):
    process()
    
    



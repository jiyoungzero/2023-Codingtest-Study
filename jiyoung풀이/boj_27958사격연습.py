# 구현, 백트래킹, 완탐

import sys
input =sys.stdin.readline
import copy
# 1~9 : 초기체력 존재
# 10이상 : 그냥 부실 수 있음 
# 1~9 죽이면 : 상하좌우에 0인 곳에 기존 초기체력/4을 전달 
# 총알 : 행 기준으로 왼쪽에서 오른쪽으로 이동 

n = int(input())
k = int(input())
arr = [list(map(int, input().split())) for _ in range(n)]
attacks = list(map(int, input().split()))

dx, dy = [0,0,1,-1],[1,-1,0,0]

x, y = 0, 0
answer = backtracking(arr, attacks)
result = 0
def backtracking(arr, attacks):
    if sum(attacks) == 0:
        return result
    
    for i in range(n):
        for j in range(n):
            if 10 <= arr[i][j]:
                arr[i][j] = 0
                backtracking(arr, )
    
    

# for attack in attacks:
#     target = 0
#     x, y = 0, 0 # 타겟 위치
    
#     for i,row in enumerate(arr):
#         for j,ele in enumerate(row):
#             # 보너스 점수이면
#             if ele >= 10 : 
#                 target = ele
#                 arr[i][j] = 0
#             # 일반 점수이면
#             elif 1<= ele < 10 and ele <= attack:  
#                 target = max(target, ele)
#                 x, y = i, j
#                 break
#     # 일반 점수일 경우
#     if 1<=target<10:
#         for k in range(4):
#             nx, ny = x+dx[k], y+dy[k]
#             if 0<=nx<n and 0<=ny<n:
#                 if arr[nx][ny] == 0:
#                     arr[nx][ny] = target//4
#     print(attack, target)
# print(arr)
                


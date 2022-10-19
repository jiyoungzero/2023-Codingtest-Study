# 문제 스스로 풀어보기 

# dfs로 일단 탐색 / 회전 연산의 개수가 6! = 720

# 1. rotate함수 : 시계 방향으로 - 슬라이싱 
# 2. findmin 함수 : 각 행의 수 중 최솟값 찾기
# 3. 연산 순서 : 순열  // 직접 구현하는 것 보다 라이브러리가 훨씬 빠름

from copy import deepcopy
import sys
input =sys.stdin.readline
from itertools import permutations

n, m, k = map(int, input().split())

a = [list(map(int, input().split())) for _ in range(n)]
rcs = [] # (r, c, s)배열 
result = 999999
for _ in range(k):
    rcs.append(list(map(int, input().split())))
    
# 1. rcs의 순열 경우의 수만큼 
# 2. 회전 copy_a = deepcopy(a)
# 3. 각 행의 최소값 구하기 

for p in permutations(rcs, k): # rcs배열을 k번 만큼의 순열 --> 모든 경우의 수
    copy_a = deepcopy(a)
    for r, c, s in p:    
        r -= 1
        c -= 1
        for i in range(1, s+1):
            # 위
            copy_a[r-i:r+i-1][c-i] = a[r-i+1:r+i][c-i] # 왜 이걸로 하면 인덱스 에러가 나지??
            
            # 오른쪽
            copy_a[r-i][c-i+1:c+i] = a[r-i][c-i:c+i-1]
            # 아래
            # copy_a[r-i+1:r+i][c+i] = a[r-i:r+i-1][c+i]
            # 왼쪽
            copy_a[r+i][c-i:c+i-1] = a[r+i][c-i+1:c+i]
    for row in copy_a:
        result = min(result, (sum(row)))
        

print(result)

# 풀이 엄청 비슷한 거 찾았는데 저 위에 거랑 for문 돌린 거랑 뭐가 다른지 모르겠음 
# from itertools import permutations
# from copy import deepcopy

# N, M, K = map(int, input().split())
# a = [list(map(int, input().split())) for _ in range(N)]
# rcs = [list(map(int, input().split())) for _ in range(K)]

# ans = 987654321

# # 1. 회전 순서 정하기 (최대 6!=720)
# for p in permutations(rcs, K):
#     # 2. 회전
#     copy_a = deepcopy(a)  # 원본리스트 카피
#     for r, c, s in p:
#         r -= 1
#         c -= 1
#         for n in range(s, 0, -1):
#             tmp = copy_a[r-n][c+n]
#             copy_a[r-n][c-n+1:c+n+1] = copy_a[r-n][c-n:c+n]  # ->
#             for row in range(r-n, r+n):  # ↑
#                 copy_a[row][c-n] = copy_a[row+1][c-n]
#             copy_a[r+n][c-n:c+n] = copy_a[r+n][c-n+1:c+n+1]  # <-
#             for row in range(r+n, r-n, -1):  # ↓
#                 copy_a[row][c+n] = copy_a[row-1][c+n]
#             copy_a[r-n+1][c+n] = tmp

#     # 3. 각 행의 최소값 찾기
#     for row in copy_a:
#         ans = min(ans, sum(row))

# print(ans)

    
# 문제 스스로 풀어보기

# 100,000을 넘지 않는 양의 정수를 합한 값이므로 완전탐색을 써도 무방하다(시간)
#  M을 넘지 않으면서 M에 최대한 가까운 카드 3장의 합을 출력
# 20분 소요


from importlib.abc import Traversable
import sys
input = sys.stdin.readline

N, M = tuple(map(int, input().split()))
cards = list(map(int, input().split())) # N장의 카트 입력
min_value, result = 200000, 0
 
# 범위 내에 있는지
def in_range(n):
    if n>0 and n <= M:
        return True
    else:
        return False

for i in range(N):
    for j in range(i+1, N):
        for k in range(j+1, N):
            value = cards[i] + cards[j] + cards[k]
            if in_range(value) and min_value > (M-value):
                min_value = M-value
                result = value

print(result)
    
# # 정답코드

# n, m = list(map(int, input().split(' ')))
# data = list(map(int, input().split(' ')))

# result, cnt = 0, 0
# length = len(data)

# for i in range(length):
#     for j in range(i+1, length):
#         for k in range(j+1, length):
#             sum_value = data[i] + data[j] + data[k]
#             if sum_value <= m:
#                 result = max(result, sum_value) # 이부분 중요

# print(result)


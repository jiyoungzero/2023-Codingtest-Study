# 실버1
# 1. W개를 넘기지 않는다
# 2. Lkg을 넘지 않는다
# 3. append 할때마다 시간은 +1됨

# 값을 더했을 때 l보다 적고 w개 보다 적으면
#  무조건 w만큼 시간 더하기

# n, w, l = map(int, input().split())
# arr = list(map(int, input().split()))
# temp = 0  # 다리 위에 있는 트럭의 무게 임시 저장
# time = 0

# result = []

# while arr:
#     i = 0
#     for i in range(0, w):
#         if len(arr) > 1:
#             temp += arr[i]
#             # print('temp ', temp)
#             if temp <= l:
#                 result.append(arr[i])
#                 # print('arr', arr)
#             else:
#                 temp -= arr[i]
#         time += 1
#         # print('time', time)
#     arr.pop(0)
#     # print(arr)

# print(time)

# # 정답
import sys
input = sys.stdin.readline

n, w, L = map(int, input().split())
trucks = list(map(int, input().split()))

bridge = [0] * w

time = 0
while bridge:
    time += 1
    bridge.pop(0)

    if trucks:
        if trucks and sum(bridge) + trucks[0] <= L:  # sum 함수 기억해두기
            bridge.append(trucks.pop(0))
        else:
            bridge.append(0)

print(time)

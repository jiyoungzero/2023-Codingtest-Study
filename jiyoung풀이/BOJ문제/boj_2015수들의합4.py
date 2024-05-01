import sys
input = sys.stdin.readline 
from collections import defaultdict


# 누적합 : 배열이 아닌, 딕셔너리로 풀이
n, k = map(int, input().split())
arr = list(map(int, input().split()))
answer = 0
prefix = [0]
for i in range(n):
    prefix.append(prefix[-1] + arr[i])

dict = defaultdict(int)
for i in range(n+1):
    answer += dict.get(prefix[i]-k, 0)
    dict[prefix[i]] += 1

print(answer)
    





# @@@ 시간초과 
# prefix = [0]*n
# prefix[0] =arr[0]
# answer = 0

# for i in range(1, n):
#     prefix[i] = prefix[i-1] + arr[i]
# prefix = [0] + prefix

# # print(prefix)
# for i in range(1, n+1):
#     for j in range(i, n+1):
#         if prefix[j] - prefix[i-1] == k:
#             # print(i, j)
#             answer += 1
# print(answer)


    
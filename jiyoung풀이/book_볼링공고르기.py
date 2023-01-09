# greedy 

import sys
input = sys.stdin.readline

n, m = map(int, input().split()) # n: 볼링 수, m : 공의 최대 무게
arr = list(map(int, input().split()))
cnt = 0

# # 내풀이 -> 구현 쪽
# for i in range(len(arr)):
#     for j in range(i+1, len(arr)):
#         if arr[i] == arr[j]:continue
#         else:
#             cnt += 1
# print(cnt)

# 그리디하게 풀이
arr.sort()# 1 2 2 3 3
w = [0] * (11) # 최대무게 한도는 10

for ele in arr:
    w[ele] = arr.count(ele)
    
result = 0
for i in range(m+1):
    if w[i] >= 1:
        n -= w[i]
        result += (n * w[i])
print(result)        
    


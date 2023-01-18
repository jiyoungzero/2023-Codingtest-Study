# 정렬

import sys
input =sys.stdin.readline

# 일단 완탐은 -> 시간 괜찮나
n = int(input())
arr = list(map(int, input().split()))
result = []

# for i in range(1, max(arr)+1):
#     tmp = 0
#     for ele in arr:
#         tmp += abs((i-ele))
#     result.append((tmp,i))
# result.sort()  
# print(result[0][1])    

# 이 문제는 중간값으로 계산하면 되므로
arr.sort()

# 중간값
median_index = arr[(n-1)//2]
print(median_index) # median_index = arr[(n-1)//2]

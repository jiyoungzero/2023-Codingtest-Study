# greedy

import sys
input = sys.stdin.readline

n = int(input())
arr = list(map(int, input().split()))

# arr.sort(reverse=True) # 오름차순으로 해야 최대그룹수가 나옴!!!
# cnt = 0

# while arr:
#     c = arr[0]
#     for _ in range(c): # 1 2 2 2 3
#         del arr[0]
#     cnt += 1
    
# print(cnt)

# 모범답안
arr.sort() # 오름차순 정렬

result = 0
cnt = 0
for ele in arr:
    cnt += 1
    if cnt >= ele:
        result += 1 # 현재 모집된 인원이 공포도 이상이라면 그룹 형성
        cnt = 0
print(result)        
    



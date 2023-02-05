# 투포인터, 이진탐색

# 1. arr 오름차순으로 정렬하기
# 2. idx로, start-end의 값을 0, (n-1)로 설정
# 3. 만약 arr[start] + arr[end]의 값이
#   - 0보다 크면, end-1
#   - 0보다 작으면, start+1
# 4. 탈출조건은 min_tmp < start + end 이면
import sys
input = sys.stdin.readline

n = int(input())
arr = list(map(int, input().split()))
min_tmp = int(1e9)
arr.sort()
start, end = 0, n-1
result = (0,0)

def in_range(a, b):
    return 0<=a<n and 0<=b<n

while start < end:
    if min_tmp < arr[start]+arr[end]:
        break
    if arr[start] + arr[end] > 0:
        if min_tmp > arr[start] + arr[end]:
            min_tmp = arr[start] + arr[end]
            result = (start, end)
            end-=1
    elif arr[start] + arr[end] < 0: 
        if min_tmp > arr[start] + arr[end]:
            min_tmp = arr[start]+ arr[end]
            result = (start, end)
            start += 1
    else: # 0으로 바로 나오는 경우
        result = (start, end)
        break
    
print(arr[result[0]], arr[result[1]])
        
    
    



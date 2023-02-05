# 투포인터, 이진탐색

# 1. arr 오름차순으로 정렬하기
# 2. idx로 투포인터 실행 / start-end의 초기값을 0, (n-1)로 설정
# 3. 만약 arr[start] + arr[end]의 값이
#   - 0보다 크면, end-1
#   - 0보다 작으면, start+1
# 4. 탈출조건은 min_tmp < abs(arr[start] + arr[end])
import sys
input = sys.stdin.readline

# n = int(input())
# arr = list(map(int, input().split()))
# min_tmp = int(2e9+1)
# arr.sort()
# start, end = 0, n-1
# result = (0,0)


# while start < end:
#     # print("요소=",arr[start],arr[end], "/ 0으로 부터의 차이=", arr[start]+arr[end], "/min_tmp = ", min_tmp )
#     if min_tmp < abs(0-(arr[start]+arr[end])): # 다음 경우가 0에서 더 벗어나면 탈출
#         break
#     if arr[start] + arr[end] > 0:
#         if min_tmp > abs(0-(arr[start] + arr[end])):
#             min_tmp = abs(0-(arr[start] + arr[end]))
#             result = (start, end)
#             end-=1
#     elif arr[start] + arr[end] < 0: 
#         if min_tmp > abs(0-(arr[start] + arr[end])):
#             min_tmp = abs(0-(arr[start]+ arr[end]))
#             result = (start, end)
#             start += 1
#     else: # 0으로 바로 나오는 경우
#         result = (start, end)
#         break
    
# print(arr[result[0]], arr[result[1]]) 




# 다른 사람 풀이
n = int(input())
arr = list(map(int, input().split()))
arr.sort()

start, end = 0, n-1
min_tmp = int(2e9+1) # 양수, 음수 둘 다 1e9의 범위를 가지니까
result = []

while start < end:
    arr_start = arr[start]
    arr_end = arr[end]
    
    total = arr_start  + arr_end
    if abs(total) < min_tmp:
        min_tmp = abs(total)
        result = [arr_start, arr_end]
    if total < 0:
        start += 1
    else:
        end -= 1
print(result[0], result[1])
    
    



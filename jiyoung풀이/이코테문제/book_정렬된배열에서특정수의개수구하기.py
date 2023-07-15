# 이진탐색
import sys
from bisect import bisect_left, bisect_right
input = sys.stdin.readline


# 시간복잡도 logN이 아니면 시간초과 

n, x = map(int, input().split())
arr = list(map(int, input().split()))

start = bisect_left(arr, x)
end = bisect_right(arr, x)
result = end-start
if result > 0:print(result)
else:print(-1)

# 구현으로 푸는 방법

def count_by_value(arr, x):
    n = len(arr)
    a = first(arr, x, 0, n-1)
    if a == None:
        return 0
    b = last(arr, x, 0, n-1)
    return b-a+1

def first(arr, target, start, end):
    if start > end:
        return None
    mid = (start+end)//2
    
    if (mid == 0 or target > arr[mid-1]) and arr[mid] == target:
        return mid
    # 중간점의 값보다 찾고자 하는 값이 작거나 같은 경우 왼쪽 확인
    elif arr[mid] >= target:
        return first(arr, target, start, mid-1)
    else: # 중간점의 값보다 타겟값이 더 큰 경우
        return first(arr, target, mid+1, end)  
    
def last(arr, target, start, end):
    if start>end:return None
    mid = (start+end) // 2
    # 해당 값을 가지는 원소 중 가장 오른쪽에 있는 것만 인덱스 반환
    if (mid == (n-1) or target < arr[mid+1]) and arr[mid] == target:
        return mid
    elif arr[mid] > target:
        return last(arr, target, start, mid-1)
    else: # 중간점의 값보다 타겟값이 더 큰 경우
        return last(arr, target, mid+1, end) 

n,x = map(int, input().split())
arr = list(map(int, input().split()))

count = count_by_value(arr, x)

if count == 0:
    print(-1)
else:
    print(count)




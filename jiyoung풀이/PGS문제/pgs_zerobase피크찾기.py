# 이진탐색 

def solution(arr):
    answer = 0
    left, right = 0,len(arr)-1

    while left < right:
        mid = (left + right) // 2
        if arr[mid] <= arr[mid+1]:
            left = mid + 1
        else:
            right = mid
    return left if left != len(arr)-1 and right != 0 else -1
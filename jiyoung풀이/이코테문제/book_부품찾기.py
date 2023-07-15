# 이진트리 

import sys
input = sys.stdin.readline

n = int(input())
arr = list(map(int, input().split()))
m = int(input())
want = list(map(int, input().split()))

def binary(arr, target, start, end):
    mid = (start+end) // 2
    
    while start <= end:
        mid = (start+end) // 2
        if arr[mid] == target:
            return mid
        elif arr[mid] < target:
            start = mid+1
        else:
            end = mid - 1
    return None # arr에 target값이 없으면 none 반환

for target in want:
    if binary(arr, target, 0, len(arr)-1) == None:
        print("no", end=" ")
    else:
        print("yes", end=" ")





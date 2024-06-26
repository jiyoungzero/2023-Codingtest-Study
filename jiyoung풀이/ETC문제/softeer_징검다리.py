import sys 
input = sys.stdin.readline 


n = int(input())
arr = list(map(int, input().split()))

def binary_search(lis, target):
    left, right = 0, len(lis)
    while left <= right:
        mid = (left+right)//2
        
        if target < lis[mid]:
            right = mid - 1
        else:
            left = mid + 1
    return left 

lis = [arr[0]]
for i in range(1, n):
    if arr[i] > lis[-1]:
        lis.append(arr[i])
    else:
        idx = binary_search(lis, arr[i])
        lis[idx] = arr[i]
print(len(lis))
        
    
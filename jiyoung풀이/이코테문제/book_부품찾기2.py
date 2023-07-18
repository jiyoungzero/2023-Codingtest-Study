import sys
input = sys.stdin.readline

n = int(input())
arr = list(map(int, input().split()))
arr.sort()

m = int(input())
checklist = list(map(int, input().split()))


def binary_search(lst, target, start, end):
    while start <= end:
        mid = (start + end) // 2
        
        if lst[mid] == target:
            return mid
        
        elif lst[mid] > target:
            end = mid-1
        else:
            start = mid + 1
    return None


for ele in checklist:
    result = binary_search(arr, ele, 0, n-1)
    if result != None:
        print("yes", end = " ")
    else:
        print("no", end=" ")
    
    

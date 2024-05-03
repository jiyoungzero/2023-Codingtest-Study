import sys
input = sys.stdin.readline 

n = int(input())
arr = list(map(int, input().split()))
answer = 0
# arr.sort() # 1 2 4 5

# (2-1)*min(1,2)
# ()

s, e = 0, n-1
while s < e:
    tmp = (e-s-1)*min(arr[s], arr[e])
    if tmp > answer:
        answer = tmp
    if arr[s] < arr[e]: 
        s += 1
    else:
        e -= 1
print(answer)
    
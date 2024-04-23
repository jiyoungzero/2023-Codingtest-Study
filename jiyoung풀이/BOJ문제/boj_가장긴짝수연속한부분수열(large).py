import sys
input = sys.stdin.readline 

n, k = map(int, input().split())
arr = list(map(int, input().split()))
prefix_odd = [0]*n 
answer = 0

prefix_odd[0] = 0 if arr[0] == 2 else 1
for i in range(1, n):
    if arr[i]%2 == 1:
        prefix_odd[i] = prefix_odd[i-1] + 1
    else:
        prefix_odd[i] = prefix_odd[i-1]
prefix_odd = [0] + prefix_odd
arr = [0] + arr

s, e = 1, n
while s <= e:
    if arr[s]%2 == 1 and arr[e]%2 == 1:
        s += 1
        e -= 1
    elif arr[s]%2 == 1 and arr[e]%2 == 0:
        s += 1
    elif arr[s]%2 == 0 and arr[e]%2 == 1:
        e -= 1
    elif arr[s]%2==0 and arr[e]%2==0 and prefix_odd[e]-prefix_odd[s-1] > k:
        s += 1
    
    if prefix_odd[e]-prefix_odd[s-1] <= k:
        answer = (e-s+1)-(prefix_odd[e]-prefix_odd[s-1])
        break

print(answer)
    
    
    
    

        
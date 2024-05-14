import sys 
input = sys.stdin.readline

n = int(input())
arr = list(map(int, input().split()))
q = int(input())

prefix = [0]*n
for i in range(1, n):
    if arr[i] < arr[i-1]:
        prefix[i] = prefix[i-1] + 1
    else:
        prefix[i] = prefix[i-1]

for _ in range(q):
    a, b = map(int, input().split())
    a -= 1
    b -= 1
    print(prefix[b]-prefix[a])
    
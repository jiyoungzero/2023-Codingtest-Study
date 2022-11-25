N = int(input())
arr = list(map(int, input().split()))
arr.sort()

# 더하는 도중에 하나라도 1 이상 증가하면 break
sum = 0
for i in range(N):
    if sum + 2 <= arr[i]:
        break
    sum += arr[i]

print(sum+1)

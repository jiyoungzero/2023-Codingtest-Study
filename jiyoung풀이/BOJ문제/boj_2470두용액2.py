import sys
input = sys.stdin.readline 

n = int(input())
arr = list(map(int, input().split()))
answer = []
s, e = 0, n-1
arr.sort() # 1 2 3 4 5 6

result = int(1e9)*2+1
while s < e:
    tmp = arr[s] + arr[e]
    
    if tmp == 0:
        answer = [arr[s], arr[e]]
        break
    
    if result > abs(tmp):
        result = abs(tmp)
        answer = [arr[s], arr[e]]

    if tmp < 0:
        s += 1
    else:
        e -= 1
        
# answer.sort()
print(*answer)

# dp

# 5-3-2순으로 나누어보고 안나눠지면 1빼고 다시 5-3-2순으로 나누기

import sys
input =sys.stdin.readline

n =int(input())
cnt = 0
arr = [5,3,2]
while n > 1:
    if n % 5 != 0 and n % 3 != 0 and n % 2 != 0:
        n -= 1
        cnt += 1
    for ele in arr:
        n /= ele
        cnt += 1
print(cnt)

    

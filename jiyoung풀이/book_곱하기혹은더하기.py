# greedy

import sys 
input = sys.stdin.readline

n = input().rstrip()
arr = []
for i in n:
    arr.append(int(i))
    
arr.sort(reverse=True)
result = 1
for ele in arr:
    if ele > 1:
        result *= ele
    else:
        result += ele
print(result)
# greedy

import sys
input = sys.stdin.readline 

command = input().rstrip()
arr = [5]
for c in command:
    a = int(c)
    if arr[-1] == a:
        continue
    arr.append(a)

if arr.count(0) < arr.count(1):
    print(arr.count(0))
else:
    print(arr.count(1))

        
    
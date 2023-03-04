# 스택 

import sys
input =sys.stdin.readline

n = int(input())
arr = []
for _ in range(n):
    arr.append(list(map(str, input().rstrip())))
    

for a in arr:
    stack = []
    # print(a)
    for ele in a:
        if ele == ")":
            if "(" in stack:
                stack.pop()
            else:
                stack.append(ele)
        else:
            stack.append(ele)
    print("NO" if stack else "YES")


            
                
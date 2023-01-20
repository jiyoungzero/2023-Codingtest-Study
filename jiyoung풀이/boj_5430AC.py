# 
import sys
input = sys.stdin.readline

test_case = int(input())

for _ in range(test_case):
    flag = True
    p = input().rstrip()
    n = int(input())
    case = input()
    tmp = case[1:-2]
    tmp = tmp.split(",")
    arr = []
    if len(tmp) > 2:
        for ele in tmp:
            arr.append(int(ele))
    print(arr)
    
    
    
    for command in p:
        if command == "R":
            arr = arr[::-1]
        elif command == "D":
            if not arr:
                print("error")
                flag = False
            else:del arr[0]
    if flag:print(arr)
                
            
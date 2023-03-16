# 스택 
# import sys
# input = sys.stdin.readline



while 1:
    string = input()
    if string == ".":
        break
    stack = []
    flag = True
    for s in string:
        if s == "(" or s=="[":
            stack.append(s)
        elif s==")":
            if len(stack) > 0:
                if stack[-1] == "(" :stack.pop()
                else:
                    flag = False
                    break
        elif s=="]":
            if len(stack) > 0:
                if stack[-1] == "[" :stack.pop()
                else:
                    flag = False
                    break
        else:continue
    if flag and len(stack)==0:
        print("yes")
    else:print("no")


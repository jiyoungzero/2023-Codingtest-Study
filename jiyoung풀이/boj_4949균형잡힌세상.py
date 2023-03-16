# 스택 
# import sys
# input = sys.stdin.readline

input_lst = []

while 1:
    string = input()
    if string == ".":
        break
    else:input_lst.append(string)
    
for string in input_lst:
    stack = []
    flag = True
    for s in string:
        if s == "(" or s=="[":
            stack.append(s)
        elif s==")" or s == "]":
            if len(stack) > 0:
                if stack[-1] == "(" and s == ")":stack.pop()
                elif stack[-1] == "[" and s == "]":stack.pop()
                else:flag = False
        else:continue
    if len(stack) > 0 or flag == False:
        print("no")
    else:print("yes")


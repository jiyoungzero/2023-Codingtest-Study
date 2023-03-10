# 스택 

def solution(s):
    answer = True

    stack = []
    for ele in s:
        if ele == "(":
            stack.append(ele)
            continue
        else: 
            if stack:stack.pop()
            else: stack.append(ele)

    print(stack)
    if len(stack)>0 : return False

    return True
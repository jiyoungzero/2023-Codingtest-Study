def solution(s):
    stack = []
    result = ''

    for ele in s:
        if len(stack) == 0:
            stack.append(ele)
            continue

        cur = stack[-1]

        if cur == ele:
            stack.pop()
        else: 
            stack.append(ele)

    result = "".join(stack)
    return result
    
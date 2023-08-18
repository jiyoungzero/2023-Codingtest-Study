def solution(s):
    if len(s) == 1:return int(s[0])
    stack = []
    num_s = []
    result = 0
    dic = ["-", "+"]

    idx = 0
    while 1:
        num = ''
        if idx == len(s):break
        if s[idx] in dic:
            num_s.append(s[idx])
            idx += 1
        else:
            while idx < len(s) and s[idx].isdigit():
                num += s[idx]
                idx += 1
            num_s.append(int(num))

    for ele in num_s:
        if ele in dic:
            stack.append(ele)
        else:
            if stack[-1] == "-":
                result -= ele
            else:
                result += ele
    return result

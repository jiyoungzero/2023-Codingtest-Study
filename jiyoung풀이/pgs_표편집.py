# 2021 카카오 채용연계형 인턴십 

# 런타임 에러로 실패 -> 테케만 통과
def solution(n, k, cmd):
    answer = ''
    z_stack = []
    original_n = n
    start_set = set(range(n))

    last = list(range(n))

    for command in cmd:
        if len(command) > 2:
            direction, idx = command.split(" ")
            if direction == "D":
                k = (k+int(idx))%n
            else:
                k = (k-int(idx))%n
        elif command == "C":
            z_stack.append(k)
            last.remove(k)
            n -= 1
            k = k%n
        elif command == "Z":
            z_idx = z_stack.pop()
            last.insert(z_idx, z_idx)
            n += 1
            
            
    # print(start_set, last)
    tmp = start_set - set(last)
    # print(tmp)
    for i in range(original_n):
        if i in tmp:answer += "X"
        else:answer += "O"
            

    return answer
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

# linked list
def solution(n, k, cmd):
    answer = ['O']*n
    cur = k
    table = {i:[i-1,i+1] for i in range(n)}
    table[0] = [None, 1]
    table[n-1] = [n-2, None]
    stack = []
    
    for c in cmd:
        if c == 'C':
            answer[cur] = "X"
            prev, next = table[cur]
            stack.append([prev, cur, next])

                            
            if prev == None:
                table[next][0] = None
            elif next == None:
                table[prev][1] = None
            else:
                table[prev][1] = next
                table[next][0] = prev    
            
            if next == None:
                cur = table[cur][0]
            else:
                cur = table[cur][1]
                
        elif c == "Z":
            prev, now, next = stack.pop()
            answer[now] = "O"
            if next == None:
                table[prev][1] = now
            elif prev == None:
                table[next][0] = now
            else:
                table[next][0] = now
                table[prev][1] = now
        else:
            direction, move = c.split(" ")
            move = int(move)
            if direction == "U":
                for _ in range(move):
                    cur = table[cur][0]
            else:
                for _ in range(move):
                    cur = table[cur][1]
        

    return "".join(answer)
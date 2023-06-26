# 2018 카카오 블라인드 
# * : 이전 점수, 현재 점수 2배 (첫번째에 도착하면 4배가 됨)
# # : (-1)배
import re 
def solution(dartResult):
    answer = 0
    cmd = []
    result = []
    n = len(dartResult)
    visited = [False]*n
    dartResult = re.split(r'*|#|S|D|T',dartResult) # 추가
    
    for i in range(n-1, -1, -1):
        if not visited[i] and dartResult[i] == "*" or dartResult[i] == "#":
            visited[i-2], visited[i-1], visited[i] = True, True, True
            if dartResult[i-1] == "S":cmd.append([int(dartResult[i-2]),1, dartResult[i]])
            elif dartResult[i-1] == "D":cmd.append([int(dartResult[i-2]),2, dartResult[i]])
            else: cmd.append([int(dartResult[i-2]),3, dartResult[i]])
            
        elif not visited[i] and dartResult[i].isalpha():
            visited[i-1], visited[i] = True, True
            if dartResult[i] == "S":cmd.append([int(dartResult[i-1]),1])
            elif dartResult[i] == "D":cmd.append([int(dartResult[i-1]),2])
            else: cmd.append([int(dartResult[i-1]),3])
        else:continue
    cmd.reverse()
    print(cmd)
    
    for i in range(len(cmd)):
        if i==0 and len(cmd[i]) == 3 and cmd[i][2] == "*":
            result.append(int((cmd[i][0]**cmd[i][1])*4))
        elif len(cmd[i]) == 3 and cmd[i][2] == "*":
            result[-1]=int(result[-1])*2
            result.append((cmd[i][0]**cmd[i][1])*2)
        elif len(cmd[i]) == 3 and cmd[i][2] == "#":
            result.append((cmd[i][0]**cmd[i][1])*(-1))
        else:
            result.append(int(cmd[i][0]**cmd[i][1]))
    print(result)
    return sum(result)
# print(solution('1S*2T*3S'))
# 2018 카카오 블라인드 
# * : 이전 점수, 현재 점수 2배 (첫번째에 도착하면 4배가 됨)
# # : (-1)배

def solution(dartResult):
    answer = 0
    cmd = []
    
    for i in range(len(dartResult)):
        if dartResult[i] == "*" or dartResult == "#":
            del cmd[-1]
            
            if dartResult[i-1] == "S": cmd.append([int(dartResult[i-2]), 1, dartResult[i]])
            elif dartResult[i-1] == "D" :  cmd.append([int(dartResult[i-2]), 2, dartResult[i]])
            elif dartResult[i-1] == "T" :  cmd.append([int(dartResult[i-2]), 3, dartResult[i]])
            
        elif dartResult[i].isalpha():
            if dartResult[i] == "S": cmd.append([int(dartResult[i-1]), 1])
            elif dartResult[i] == "D" :  cmd.append([int(dartResult[i-1]), 2])
            elif dartResult[i] == "T" :  cmd.append([int(dartResult[i-1]), 3])

    print(cmd)
    
    # for i in range(len(cmd)):
    #     if i == 0 and len(cmd[i]) == 3 and cmd[i][2] == "*":
            
            
        

    return answer
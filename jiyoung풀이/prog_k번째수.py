def solution(array, commands):
    answer = []
    for c in commands:
        start, end, target = c[0]-1, c[1]-1, c[2]-1
        tmp = array[start:end+1]
        tmp.sort()
        answer.append(tmp[target])
    return answer
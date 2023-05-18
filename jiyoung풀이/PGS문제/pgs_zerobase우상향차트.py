# 입력설명
# 0 < values.length <= 100000
# 출력설명
# 단조 증가 구간을 길이가 2인 정수 배열로 반환

# 매개변수 형식
# values = {103, 152, 124, 165, 152, 154, 159, 160, 200, 195, 205, 206, 204, 189, 156}

# 반환값 형식
# {4, 8}

def solution(values):
    answer = [0,0]
    n = len(values)

    for i in range(n-1):
        original_s = i
        s, e = i, i+1

        while  e < n and values[s] < values[e]:
            s = e
            e += 1
        if answer[1] - answer[0] < e-1 - original_s:
            answer = [original_s, e-1]

#
    return answer  if answer != [0,0] else [0,0]
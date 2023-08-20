# 구현

def possible(answer):
    return True

def solution(n, build_frame):
    answer = []
    
    for frame in build_frame:
        x, y, stuff,  operate = frame
        if operate == 0: # 삭제
            answer.remove([x, y, stuff])
            if not possible(answer):
                answer.append([x, y, stuff])
        if operate == 1 : # 설치
            answer.append([x, y, stuff])
            if not possible(answer):
                answer.remove([x, y, stuff])
    return sorted(answer)
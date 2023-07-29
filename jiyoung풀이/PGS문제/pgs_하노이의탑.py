# 재귀 

def solution(n):
    answer = [] # [a,b] a에 있는 것을 b번으로 보내기 

    def hanoi(n, start, end, mid):
        if n == 1:
            answer.append([start, end])
            return 
        hanoi(n-1, start, mid, end)
        answer.append([start, end])
        hanoi(n-1, mid, end, start)

    hanoi(n, 1,3, 2)


    return answer
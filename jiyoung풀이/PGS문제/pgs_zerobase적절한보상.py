# 꼭 다시 풀어보기

# 문제 : 최소 1개 이상의 초코렛은 각 학생에게 나누어 주어야 한다.
#       바로 인접한 친구보다 점수가 높다면, 더 많은 초코렛을 받아야 한다.
#       위 조건을 만족하면서 최소로 초코렛을 나누어 줄 때, 각 학생이 받는 초코렛의 개수를 출력하시오.

# 입력설명
# 0 < scores.length <= 1000000
# 출력설명
# 각 학생이 받게 되는 초코렛의 개수를 정수 배열로 반환

# 매개변수 형식
# scores = {1, 3, 5, 4, 5, 5, 5, 1}

# 반환값 형식
# {1, 2, 3, 1, 2, 1, 2, 1}

def solution(scores):
    chocos = [1 for _ in range(len(scores))]
    
    for i in range(len(scores) - 1):
        if scores[i+1] > scores[i]:
            chocos[i+1] = chocos[i] + 1
    
    for i in range(len(scores)-2, -1, -1):
        if scores[i+1] < scores[i]:
            chocos[i] = max(chocos[i+1] + 1, chocos[i])
    return chocos

                
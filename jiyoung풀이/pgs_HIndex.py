# 정렬


def solution(citations):
    answer = 0
    citations.sort(reverse=True)
    n = len(citations)
    if set(citations) == {0}:return 0
    
    for i in range(n):
        if citations[i] > i:
            answer = i
        else:
            break

    answer += 1
    return answer
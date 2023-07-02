# 카카오 2018 블라인드

def makeElements(lst):
    n = len(lst)
    result = []

    for i in range(n-1):
        target = lst[i:i+2]
        if target[0].isalpha() and target[1].isalpha():
            result.append(target)
        else:
            continue
    return result


def solution(str1, str2):
    answer = 0
    inter, union = 0, 0
    str1 = str1.lower()
    str2 = str2.lower()

    # 두 개씩 끊기
    str1List = makeElements(str1)
    str2List = makeElements(str2)

    # 중복 없는 모든 원소 : 합집합 = |, 교집합 = &
    case = set(str1List) | set(str2List)

    # 교집합 min(str1List.count(s), str2List.count(s))
    # 합집합 max(str1List.count(s), str2List.count(s))
    for c in case:
        inter += min(str1List.count(c), str2List.count(c))
        union += max(str1List.count(c), str2List.count(c))

    if union > 0 :
        answer = inter/union  
    else:
        answer = 1

    return int(answer*65536)
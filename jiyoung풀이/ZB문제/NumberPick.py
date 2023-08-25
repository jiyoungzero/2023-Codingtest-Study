# 문제: 정수 배열 A에는 0~9까지의 숫자가 랜덤 하게 들어있습니다.

# 해당 배열에서 숫자를 2개 뽑아 조합해서 만들 수 있는 두 자리 정수 중, K번째로 큰 숫자를 출력하는 프로그램을 구현하세요.


import itertools
def solution(A, K):
    lst = list(itertools.permutations(A, 2))
    sort_lst = []
    for ele in lst:
        a, b = ele
        sort_lst.append(a*10+b)
    sort_lst.sort(reverse=True)
    return sort_lst[K-1]
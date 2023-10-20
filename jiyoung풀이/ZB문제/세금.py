# 지난 해 한 국가에서는 N명이 세금을 납부했다. 세금을 관리하는 직원은 지난 해 사람들이 세금을 낸 정보를 수합하는 과정에서 K번의 정보 수집을 진행하고자 한다. 각 정보 수집에서는 X와 Y 두 가지 변수가 사용되는데, 이는 납부한 세금의 금액이 X 이상 Y 이하인 사람의 수를 계산하는 작업을 의미한다.

# 각 K번의 정보 수집에 대하여, 납부한 세금의 금액이 X 이상 Y 이하인 사람의 수를 차례대로 계산하는 프로그램을 작성하여라.

# 예를 들어 N=5명이 납부한 세금의 금액이 다음의 표와 같다고 해보자.


# 금액
# 7
# 2
# 3
# 5
# 2


# 이후에 K=3번의 정보 수집에 대한 정보가 다음과 같다고 가정하자. 정보 수집을 위해 사용되는 변수는 [X, Y] 배열 형태로 주어진다.


# [1, 100]
# [3, 5]
# [2, 2]

# 현재 예시에서 각 정보 수집에 대한 정답 결과는 다음과 같다. 현재 예시에서 정보 수집 결과는 차례대로 5명, 2명, 2명이다.
# ---> 이진 탐색 문제이다 

from bisect import bisect_left, bisect_right

# 값이 [left_value, right_value]인 데이터의 개수를 반환하는 함수
def count_by_range(array, left_value, right_value):
    right_index = bisect_right(array, right_value)
    left_index = bisect_left(array, left_value)
    return right_index - left_index

# 사람의 수(N), 정보 수집 횟수(K), 세금 정보 배열(arr), 쿼리 배열(queries)
def solution(N, K, arr, queries):
    arr.sort()  # 이진 탐색을 수행하기 위한 정렬
    answer = []
    for query in queries:
        x, y = query
        # 값이 [x, y] 범위에 있는 데이터의 개수 계산
        cnt = count_by_range(arr, x, y)
        answer.append(cnt)  # 결과 기록
    return answer


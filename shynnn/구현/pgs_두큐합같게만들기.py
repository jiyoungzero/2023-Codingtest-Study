# deque를 안쓰고 list.pop(0)으로 하게 되면 실패
# why ? : 시간차이
# list의 경우 pop()으로 마지막 값을 꺼내는 경우 O(1) (일정한 시간) 시간이 걸리는데,
# pop(0)으로 가장 앞단에 값을 꺼낼때는 list 크기에 따라 읽어 오는 시간이 달라진다. O(n) 시간이 걸린다.
# deque를 사용할 경우 O(1) 시간이 걸린다. index의 주소값으로 바로 값을 찾기 때문
from collections import deque


def solution(queue1, queue2):
    qu_1 = deque(queue1)
    qu_2 = deque(queue2)
    sum_1 = sum(qu_1)
    sum_2 = sum(qu_2)

    for i in range(len(queue1) * 3):
        if sum_1 == sum_2:
            return i
        if sum_1 > sum_2:
            num = qu_1.popleft()
            qu_2.append(num)
            sum_1 -= num
            sum_2 += num
        else:
            num = qu_2.popleft()
            qu_1.append(num)
            sum_2 -= num
            sum_1 += num
    return -1

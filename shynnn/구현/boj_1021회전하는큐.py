# 자료구조, 덱(양방향 큐- 즉 스택+큐)
# 하, 30분
# 30분 초과 . 실패.. 알고리즘을 생각 후 코드를 짜는 습관을 가져야 할 것
# n = 큐 크기, m =뽑을 수의 개수

# n, m = map(int,  input().split(' '))
# n <= 50, m<n
# location = list(map(int, input().split(' ')))
# print('location:', location)
# deque = [i for i in range(1, n+1)]
# print(deque)
# count = 0

# while location:
#     if location[0] > deque[0]:
#         print(deque[0], location[0])
#         print('deque0', deque[0])
#         deque.append(deque.pop(0))
#         count += 1
#         print('첫번째', count)
#     elif location[0] < deque[0]:
#         deque.insert(0, deque.pop())
#         count += 1
#         print('두번째', count)
#     elif deque[0] == location[0]:
#         location.pop(0)
#         print('location:', location)

# print(count)

# 정답
# popleft가 있구나~!
# 무조건 왼쪽에서 접근하려다 보니 틀림
# 매번 왼쪽과 오른쪽 중 어디가 가까운지 확인하여 더 가까운 쪽으로 돌리기 해야함.
from collections import deque
import sys
input = sys.stdin.readline

n, m = map(int,  input().split(' '))
d = deque([i for i in range(1, n+1)])
targets = list(map(int, input().split(' ')))
cnt = 0

for target in targets:
    index = d.index(target)
    if index <= len(d) // 2:  # 왼쪽으로 돌리는 게 더 빠른 경우
        for i in range(index):  # 회전 연산 반복 수행
            x = d.popleft()
            d.append(x)
            cnt += 1
    else:  # 오른쪽으로 돌리는 게 더 빠른 경우
        for i in range(len(d) - index):  # 회전 연산 반복 수행
            x = d.pop()
            d.appendleft(x)
            cnt += 1
    d.popleft()  # 원소 꺼내기
print(cnt)  # 결과 출력

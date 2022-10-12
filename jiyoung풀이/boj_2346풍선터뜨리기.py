# 문제 스스로 풀어보기

# "단, 1번 풍선의 왼쪽에 N번 풍선이 있고, N번 풍선의 오른쪽에 1번 풍선이 있다. " --> 이 부분에서 회전 큐임을 알았음 
# 30분 초과 --> 왜 16번줄 안되는지 보기
# from collections import deque
# import sys
# input = sys.stdin.readline

# n = int(input())
# lst = list(map(int, input().split())) # 각 풍선에 들어있는 정수 
# que = deque([i for i in range(1, n+1)])
# result = [1,]

# current = que.popleft()

# # for _ in range(len(que)-1): # 이게 왜 아닐까?? 위에서 이미 하나 빼놓고 시작해서 -1한건데...
# for _ in range(len(que)):
#     value = lst[current-1]
    
#     if value > 0 : # 왼쪽 회전 
#         for _ in range(value-1):
#             l = que.popleft()
#             que.append(l)
#     else: # 오른쪽 회전
#         for _ in range(-value):
#             r = que.pop()
#             que.appendleft(r)
#     current = que.popleft()
#     result.append(current)

# for ele in result:
#     print(ele, end=" ")
    
    
# 정답 코드 

# 빠른 입력 함수 사용
import sys
input = sys.stdin.readline
from collections import deque
n = int(input())  # 원소의 개수 N
# 전체 원소 리스트
arr = list(map(int, input().split()))
d = deque()  # 덱(deque) 초기화
for i in range(n):
    # (수, 번호) 형태로 원소를 삽입
    d.append((arr[i], i + 1))
    result = []  # 결과 배열

current, index = d.popleft()  # 원소 추출
result.append(index)
for i in range(n - 1):  # 원소를 모두 꺼내기
    if current > 0:  # 양수라면
    # current - 1번 "왼쪽으로 돌리기" 수행
        for j in range(current - 1):
            x = d.popleft()
            d.append(x)
    else:  # 음수라면 (0은 없음)
        # |current|번 "오른쪽으로 돌리기" 수행
        for j in range(-current):
            x = d.pop()
            d.appendleft(x)
    # 원소 추출
    current, index = d.popleft()
    result.append(index)
for x in result:  # 결과 출력
    print(x, end=' ')


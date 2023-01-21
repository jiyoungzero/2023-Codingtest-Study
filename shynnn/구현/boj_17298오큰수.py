# 골드4
# 1. 자료구조를 사용해 시간복잡도를 최소화 하자.
#  ->for 문 X 2 , for 문 X stack 의 시간복잡도 비교

# 2. Stack은 어떤 문제 유형에서 활용할 수 있는가? 에 대해 적응할 필요가 있다.
# -> 문제를 풀면서 처음에 stack을 쓸 수 있을지 생각 자체가 나지 않았음.

# 3. 조건을 만족하지 않는 경우를 default 값으로 하는 풀이
# result = [-1] * N

N = int(input())
arr = list(map(int, input().split()))
result = [-1] * N
stack = [0]

for i in range(1, N):
    while stack and arr[stack[-1]] < arr[i]:
        result[stack.pop()] = arr[i]
    stack.append(i)

print(*result)

'''
# 자료구조, 스택
# 중상, 50분
# 못풀었음..
# import sys
# input = sys.stdin.readline

# n = int(input())
# a = list(map(int, input().split(' ')))
# result = []
# stack = []


# def NGE(a):
#     for i in range(n):
#         for j in range(i, n-i):
#             if a[i] < a[j]:
#                 return a[j]
#             else:
#                 continue


# result.append(NGE(a))

# print(' '.join(result))

# 정답
# 오큰수를 아직 찾지 못한 처리 중인 원소를 담기 위해 스택을 사용
# 내림차순이면 stack에 넣기
# 큰 수를 만나면 stack에서 pop. 작은 수를 만나기 전까지 -> 오큰수 처리
# 어렵네.. 다시 풀기
n = int(input())  # 수의 개수
arr = list(map(int, input().split()))  # 수열 데이터
stack = []  # 오큰수를 아직 찾지 못한 처리 중인 원소들 담을 stack
NGE = [-1] * n  # 오큰수 배열

for i in range(n):
    x = arr[i]  # 하나씩 수 확인
    if len(stack) == 0 or stack[-1][0] >= x:  # 작거나 같은 원소를 만났다면
        stack.append((x, i))  # (수, 인덱스) 형태로 삽입
    else:  # 큰 수를 만났다면
        while len(stack) > 0:  # 역방향으로 하나씩 꺼내기
            previous, index = stack.pop()
            if previous >= x:  # 크거나 같은 이전 원소를 만났다면 다시 삽입
                stack.append((previous, index))
                break
            else:
                NGE[index] = x  # 오큰수 기록
        stack.append((x, i))  # (수, 인덱스) 형태로 삽입

for x in NGE:  # 오큰수를 하나씩 출력
    print(x, end=' ')
'''

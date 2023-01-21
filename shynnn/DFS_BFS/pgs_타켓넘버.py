from collections import deque
numbers = [1, 1, 1, 1, 1]
target = 3


def dfs(numbers, target, index, value):

    if len(numbers)-1 == index:
        if target == value:
            return 1
        else:
            return 0
    index += 1

    minus_value = dfs(numbers, target, index, value - numbers[index])
    plus_value = dfs(numbers, target, index, value + numbers[index])

    return minus_value + plus_value


# 다른사람 풀이
# def solution(numbers, target):
#     if not numbers and target == 0 :
#         return 1
#     elif not numbers:
#         return 0
#     else:
#         return solution(numbers[1:], target-numbers[0]) + solution(numbers[1:], target+numbers[0])


def solution(numbers, target):
    return bfs(numbers, target)


print(solution(numbers, target))


def bfs(numbers, target):
    answer = 0
    index = 0
    q = deque()
    q.append([(-1, 0)])

    while q:
        index, value = q.popleft()

        if index == len(numbers)-1:
            if value == target:
                answer += 1
            continue

        index += 1
        q.append((index, value+numbers[index]))
        q.append((index, value-numbers[index]))

    return answer

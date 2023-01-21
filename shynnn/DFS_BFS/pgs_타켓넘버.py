numbers = [1, 1, 1, 1, 1]
target = 3


def solution(numbers, target):
    return dfs(numbers, target, -1, 0)


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


print(solution(numbers, target))


# 다른사람 풀이
# def solution(numbers, target):
#     if not numbers and target == 0 :
#         return 1
#     elif not numbers:
#         return 0
#     else:
#         return solution(numbers[1:], target-numbers[0]) + solution(numbers[1:], target+numbers[0])

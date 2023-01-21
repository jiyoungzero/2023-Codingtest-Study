#!/bin/python3

# 1. magic square 경우의 수 직접 입력

# magic square 경우의 수
# def formingMagicSquare(s):
#     possibilities = [[8, 1, 6, 3, 5, 7, 4, 9, 2],
#                      [6, 1, 8, 7, 5, 3, 2, 9, 4],
#                      [4, 9, 2, 3, 5, 7, 8, 1, 6],
#                      [2, 9, 4, 7, 5, 3, 6, 1, 8],
#                      [8, 3, 4, 1, 5, 9, 6, 7, 2],
#                      [4, 3, 8, 9, 5, 1, 2, 7, 6],
#                      [6, 7, 2, 1, 5, 9, 8, 3, 4],
#                      [2, 7, 6, 9, 5, 1, 4, 3, 8]]

#     arr = []
#     for i in range(len(s)):
#         arr += s[i]

#     result = 1000000
#     for p in possibilities:
#         temp = 0
#         for i in range(len(arr)):
#             temp += abs(arr[i]-p[i])  # 절대값
#         if temp < result:
#             result = temp
#     return result

# 2. magix square 직접 코딩해보기
def formingMagicSquare(s):
    possibilities = []
    for a in range(1, 10):
        for b in range(1, 10):
            if set([a, 15-a-b, b, 5+b-a, 5, 5+a-b, 10-b, a+b-5, 10-a]) == set(range(1, 10)):
                possibilities.append([a, 15-a-b, b,
                                      5+b-a, 5, 5+a-b,
                                      10-b, a+b-5, 10-a])
    arr = []
    for i in range(len(s)):
        arr += s[i]

    result = 1000000
    for p in possibilities:
        temp = 0
        for i in range(len(arr)):
            temp += abs(arr[i]-p[i])  # 절대값
        if temp < result:
            result = temp
    return result


if __name__ == '__main__':

    s = []

    for _ in range(3):
        s.append(list(map(int, input().rstrip().split())))
    print(formingMagicSquare(s))

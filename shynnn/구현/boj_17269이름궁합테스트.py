# 브론즈1, 문자열처리

# def StringToNUm(arr):
#     result = []
#     ascii = {'A': 3, "B": 2, "C": 1, "D": 2, "E": 4, "F": 3,
#              "G": 1, "H": 3, "I": 1, "J": 1, "K": 3, "L": 1,
#              "M": 3, "N": 2, "O": 1, "P": 2, "Q": 2, "R": 2,
#              "S": 1, "T": 2, "U": 1, "V": 1, "W": 1, "X": 2,
#              "Y": 2, "Z": 1}
#     for data in arr:
#         result.append(ascii[data])
#     return result


# def Mix(arr1, arr2, n, m):
#     result = []
#     for i in range(min(n, m)):
#         result.append(arr1[i])
#         result.append(arr2[i])
#     if n > m:
#         for data in arr1[m:n]:
#             result.append(data)
#     else:
#         i = m-n
#         for data in arr2[n:m]:
#             result.append(data)
#     return result


# def lov(arr):
#     length = len(arr)
#     result = []
#     for i in range(length-1):
#         temp = arr[i]+arr[i+1]
#         if temp >= 10:
#             temp = temp % 10
#         result.append(temp)

#     if len(result) > 2:
#         result = lov(result)  # 재귀

#     return result


# n, m = map(int, input().split())
# first, second = map(list, input().strip().split())

# mix = Mix(first, second, n, m)
# result = lov(StringToNUm(mix))

# ans = result[0]*10 + result[1]
# print(str(ans)+"%")

# 정답
# N, M = map(int, input().split())
# A, B = input().s

dic = {}
arr = [1, 2, 3]

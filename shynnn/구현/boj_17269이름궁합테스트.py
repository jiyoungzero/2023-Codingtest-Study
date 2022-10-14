# 브론즈1, 문자열처리
# zip 함수 사용

# a = int(input())
# # b = int(input())
# first = list(map(str, input()))
# second = list(map(str, input()))


# def Mix(arr1, arr2):
#     m_arr = max(arr1, arr2, key=len)
#     n_arr = min(arr1, arr2, key=len)
#     print(m_arr)
#     l = len(m_arr)+len(n_arr)
#     print('l', l)
#     mix = []
#     j = 0
#     for i in range(0, l):
#         # while m_arr:
#         print(i)
#         if n_arr:
#             # if (i % 2) == 0:
#             shin = m_arr.pop(0)
#             mix.append(shin)
#             # else:
#             ye = n_arr.pop(0)
#             mix.append(ye)
#             print(mix)
#         elif m_arr:
#             mix.append(m_arr.pop(0))
#             print(mix)
#         else:
#             break
#         j += 1
#     return mix


# def StringToNum(arr):
#     print(arr)
#     for i in range(len(arr)):
#         if arr[i] == 'E':
#             arr[i] = 4
#         elif arr[i] == 'A' or arr[i] == 'F' or arr[i] == 'H' or arr[i] == 'K' or arr[i] == 'M':
#             arr[i] = 3
#         elif arr[i] == 'B' or arr[i] == 'D' or arr[i] == 'N' or arr[i] == 'P' or arr[i] == 'Q' or arr[i] == 'R' or arr[i] == 'T' or arr[i] == 'X' or arr[i] == 'Y' or arr[i] == 'Z':
#             arr[i] = 2
#         else:
#             arr[i] = 1
#     print(arr)
#     return arr


# def lov(arr):
#     for i in range(len(arr)-2):
#         resultt = []
#         temp = arr[i]+arr[i+1]
#         if temp > 10:
#             temp = temp % 10
#         resultt.append(temp)
#     return resultt


# # result = []
# # mix_and_num = StringToNum(Mix(first, second))

# print(Mix(first, second))

# # result.append(lov(mix_and_num))
# # print(result)

def StringToNUm(arr):
    result = []
    ascii = {'A': 3, "B": 2, "C": 1, "D": 2, "E": 4, "F": 3,
             "G": 1, "H": 3, "I": 1, "J": 1, "K": 3, "L": 1,
             "M": 3, "N": 2, "O": 1, "P": 2, "Q": 2, "R": 2,
             "S": 1, "T": 2, "U": 1, "V": 1, "W": 1, "X": 2,
             "Y": 2, "Z": 1}
    for data in arr:
        result.append(ascii[data])
    return result


def Mix(arr1, arr2, n, m):
    result = []
    for i in range(min(n, m)):
        result.append(arr1[i])
        result.append(arr2[i])
    if n > m:
        for data in arr1[m:n]:
            result.append(data)
    else:
        i = m-n
        for data in arr2[n:m]:
            result.append(data)
    return result


def lov(arr):
    length = len(arr)
    result = []
    for i in range(length-1):
        temp = arr[i]+arr[i+1]
        if temp >= 10:
            temp = temp % 10
        result.append(temp)

    if len(result) > 2:
        result = lov(result)  # 재귀

    return result


n, m = map(int, input().split())
first, second = map(list, input().strip().split())

mix = Mix(first, second, n, m)
result = lov(StringToNUm(mix))

ans = result[0]*10 + result[1]
print(str(ans)+"%")

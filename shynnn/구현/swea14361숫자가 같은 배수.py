# D3
# 무조건 impossible
# 1. N이 한자리수
# 2. 첫번재 자리수가 max값

# while로 자리수 변동 없을 때까지 multiple list에 저장함

from itertools import permutations

# 108개 중 83개 맞음...


def isOneDigit(N):
    if N < 10:
        return True
    return False


def isOneDigitMax(arr_n):
    if arr_n[0] == max(arr_n):
        return True
    return False


def storeMultiple(N, length):
    global arr_multiple
    i = 2
    temp = 1
    while True:
        temp = N * i
        if length != len(str(temp)):
            break
        arr_multiple.append(temp)
        i += 1


def check():
    for a in permutations(arr_n, len(arr_n)):
        num = ""
        for aa in a:
            num += str(aa)
        if int(num) in arr_multiple:
            answer = "possible"
            return answer
    answer = "impossible"
    return answer


T = int(input())
for t in range(1, T+1):
    N = int(input())
    arr_n = list(map(int, str(N)))
    answer = 0
    arr_multiple = []

    if isOneDigit(N) or isOneDigitMax(arr_n):
        answer = "impossible"
        print("#{} {}".format(t, answer))
        continue

    storeMultiple(N, len(arr_n))
    answer = check()

    print("#{} {}".format(t, answer))

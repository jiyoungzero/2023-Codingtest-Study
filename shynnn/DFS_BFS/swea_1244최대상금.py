# 테스트케이스 15개 중 11개만 맞음
# 예외가 뭘가..흠

T = int(input())
result = 0
num = 0


def listToInt(str):
    res = 0
    for i in range(len(str)):
        temp = int(str[i])
        res += temp
        res *= 10
    return int(res/10)


def dfs(n, cur):
    global result
    global num

    if cur == num:
        result = max(result, listToInt(str))
        return

    for i in range(n, len(str)):
        for j in range(len(str)):
            str[i], str[j] = str[j], str[i]
            dfs(i, cur + 1)
            str[i], str[j] = str[j], str[i]


for t in range(1, T+1):
    str, num = input().split()

    num = int(num)
    str = list(str)

    result = 0
    if len(str) < num:
        num = len(str)

    dfs(0, 0)
    print("#{} {}".format(t, result))

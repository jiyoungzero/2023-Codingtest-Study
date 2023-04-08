# 제로베이스 문제 : 연속된 정수의 합이 `n`과 같은 경우의 수

answer = 0
result = []
def solution(n):
    for i in range(n//2+1):
        dfs(n, i)
    return answer+1

def dfs(n, prev):
    global answer
    if sum(result) == n:
        print(result)
        answer += 1
        return 

    elif sum(result) > n:return

    for i in range(1, n+1):
        if prev+1 == i:
            result.append(i)
            dfs(n, i)
            result.pop()

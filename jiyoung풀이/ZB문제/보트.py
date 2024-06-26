# 문제 설명
# 무인도에 갇힌 N명의 인원이 우연히 발견한 보트를 통해 탈출을 생각하고 있습니다.

# 보트의 경우 2인승이라 한 번에 최대 2명씩 밖에 탈 수 없고, 무게 제한이 있습니다.

# 사람들의 몸무게를 담은 정수 배열 A와 보트 무게제한 limit가 주어집니다.

# 최대한 적게 보트를 사용하여 모든 사람을 구출하려고 할 때, 필요한 보트의 사용 횟수를 구하는 프로그램을 구현하세요.

# 단, 무인도에 갇힌 사람은 1명 이상이며, 보트의 무게 제한보다 사람의 몸무게보다 큰 경우는 없습니다.
def solution(A, limit): # 90 70 51 50 49 45
    A.sort()
    answer = 0
    n = len(A)
    visited = [False]*n

    for i in range(n-1):
        if visited[i] : continue
        for j in range(n-1, i, -1):
            if not visited[i] and not visited[j]: 
                if A[i] + A[j] <= limit:
                    print("ss", i, j,A[i] + A[j], limit)
                    answer += 1
                    visited[i], visited[j] = True, True

    return (n - answer)
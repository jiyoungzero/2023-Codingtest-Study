# 복수 필수..
# 이분매칭

def solution(N, stones):
    answer = 0
    match = [-1 for _ in range(N)]
    vector = [[] for _ in range(N)]
    for s,e in stones:
        vector[s].append(e)
    
    for i in range(N):
        visited = [False for _ in range(N)]
        if dfs(i, visited, vector, match):
            answer += 1

    return answer

def dfs(x, visited, vector, match):
    for edge in vector[x]:
        if visited[edge]:continue
        visited[edge] = True

        if match[edge] == -1 or dfs(match[edge], visited, vector, match):
            match[edge] = x
            return True
    return False
        
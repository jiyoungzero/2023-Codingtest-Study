# 이게 왜 bfs, dfs..?

# bfs 이용 -> 수평적 
def solution(numbers, target):
    answer = 0
    leaves = [0]
    for num in numbers: 
        tmp = []
        for parents in leaves:
            tmp.append(parents + num)
            tmp.append(parents - num)
        leaves = tmp
    for leaf in leaves[1:]:
        if leaf == target:
            answer += 1
    
    return answer

# dfs -> 하나씩 비교해 가면서 재귀로 풀기 https://velog.io/@timointhebush/%ED%94%84%EB%A1%9C%EA%B7%B8%EB%9E%98%EB%A8%B8%EC%8A%A4-%ED%83%80%EA%B2%9F-%EB%84%98%EB%B2%84-DFS-BFS-Python


def solution(numbers, target):
    answer = dfs(numbers, target, 0)

    return answer

def dfs(numbers, target, depth):
    answer = 0
    if depth == len(numbers):
        if sum(numbers) == target:
            return 1
        else:return 0

    else:
        answer += dfs(numbers, target, depth+1) # 더하기로 시작해서 여기로 재귀에 들어가면 +1, -1 모두 겪게 된다. 
        numbers[depth] *= (-1)
        answer += dfs(numbers, target, depth+1) # 빼기로 시작해서 여기로 재귀에 들어가면 +1, -1 모두 들어가게 된다. -> 깊이 우선 탐색!!
    return answer
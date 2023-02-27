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
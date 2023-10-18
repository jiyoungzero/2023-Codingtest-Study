# N명의 학생을 K개의 그룹으로 나누고자 한다. 각 학생은 협동력 점수를 가지고 있으며, 단 하나의 그룹에만 속할 수 있다. 모든 학생은 반드시 각자 특정한 하나의 그룹에 배치된다.

# 모든 학생에 대한 그룹 배치가 끝나고 나면, 각 그룹의 전투력을 계산할 수 있다. 이때 특정한 그룹의 전투력은 그룹에 포함된 각 학생에 대하여 (해당 그룹에 속한 구성원 수 X 해당 학생의 협동력 점수)을 계산하여 모두 더한 값이다. 어떤 학생의 협동력 점수는 음수(-)일 수 있으며, 결과적으로 특정한 그룹의 전투력은 음수가 될 수도 있다.

# 이때, N명의 학생으로 K개의 그룹을 구성하는 모든 경우를 고려했을 때, 가장 전투력이 높은 그룹과 전투력이 낮은 그룹의 전투력 차이의 최솟값을 구하여라. 단, 모든 K개의 그룹에 최소한 1명의 학생은 배치되어야 한다.


# 풀이 방법 : 중복 순열 (백트래킹)


def dfs(N, K, arr, depth):
    global answer
    
    if depth == N: # N명이 K개의 선택지를 하나씩 선택한 상황
        groups = [[] for _ in range(K)]
        for i in range(N):
            index = selected[i]
            groups[index].append(arr[i])
        # 한명도 배치되지 않은 그룹이 있는 경우에는 무시
        for i in range(K):
            if len(groups[i]) == 0:return 
        min_score = int(1e9)
        max_score  = -int(1e9)
        for group in groups:
            score = 0
            for power in group:
                score += len(group) * power
            min_score = min(min_score, score)
            max_score = max(max_score, score)
        answer = min(answer, max_score-min_score)
        return 
    
    # 0번부터 K-1번까지의 학생이 그룹의 인덱스를 확인하며 선택
    for i in range(K):
        selected.append(i) 
        dfs(N, K, arr, depth+1)
        selected.pop(i)
selected = []

def solution(N, K, arr):
    global answer
    answer = int(1e9)
    dfs(N, K, arr, 0)
    return answer
        
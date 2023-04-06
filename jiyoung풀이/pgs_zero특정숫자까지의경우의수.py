# 오답 문제 설명
# 당신은 수직선 위에 서있습니다. 그리고 당신은 같은 수직선 위의 n미터 떨어진 목적지로 가려고 합니다. 당신은 한번에 수직선 위를 k 이하의 정수 거리만큼 이동할 수 있으며, 처음 이동한 방향으로만 계속 이동할 수 있습니다. 그리고 직전에 이동한 거리와 같은 거리만큼 다시 이동할 수는 없습니다.

# 예를 들어, 3-2-3 순서대로 이동했다면 다음에 3만큼 이동할 수 없습니다.

# 수직선 길이 n과 이동 가능한 최대 거리 k가 주어질 때, 목적지에 도착 가능한 경로의 경우의 수를 출력하는 함수, solution을 완성해주세요.
# 결과 값이 매우 클 수 있으니, 1,000,000,007로 나눈 나머지 값을 구해주세요.


# 내 답안 -> 시간초과
answer = 0
def solution(n, k):
    dfs(0, 0, n, k)
    return answer%1000000007

def dfs(value, prev, n, k):
    global answer
    if value == n:
        answer = (answer+1)%1000000007
        return 
    elif value > n:return
    elif value < n:
        for i in range(1, k+1):
            if i!=prev:
                dfs(value+i, i, n, k)
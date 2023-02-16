import sys

input = sys.stdin.readline
INF = int(1e9)
n = int(input())
cities = [list(map(int, input().split())) for _ in range(n)]
dp = [[None] * (1 << n) for _ in range(n)]


def find_path(last, visited):
    if visited ==(1 << n) - 1: # 2^n - 1 // 1000 - 1 = 1 1 1
        return cities[last][0] or INF  # 출발점으로 되돌아 가는 경로가 있을때, 없을 때

    if dp[last][visited] is not None: # 이미 거쳐간 곳이면 그대로 리턴 
        return dp[last][visited]

    tmp = INF # 
    for city in range(n):
        if visited & (1 << city) == 0 and cities[last][city] != 0: # (방문하지 않은 도시이거나 ) (갈 수 있는 길이 존재하면)
            tmp = min(tmp, find_path(city, visited | (1 << city)) + cities[last][city]) # 다음에 갈 곳을 비트마스킹에서 0이 나온 것을 next로 find_path
    dp[last][visited] = tmp
    return dp[last][visited]


print(find_path(0, 1 << 0))
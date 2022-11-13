T = int(input())


def dfs(x, sum):
    global result
    if x >= N:
        return
    temp = sum + A[x]
    result.append(temp)
    dfs(x+1, temp)
    dfs(x+1, sum)


for t in range(1, T+1):
    N, K = map(int, input().split())
    A = list(map(int, input().split()))
    result = []
    visited = [0]*N
    # DFS?

    dfs(0, 0)
    print("#{} {}".format(t, result.count(K)))

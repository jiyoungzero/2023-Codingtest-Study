def solution(start, end, price):
    items = [(e, s, p) for e, s, p in zip(end, start, price)]
    items.sort()

    dp = [0 for _ in range(max(end) + 1)]
    for e, s, p in items:
        for j in range(e, len(dp)):
            dp[j] = max(dp[s] + p, dp[j])
    
    return dp[-1]


    

# start = [1, 5, 10, 6, 5]
# end = [5, 6, 12, 9, 12]
# price = [10, 40, 30, 20, 50]

# print(solution(start, end, price))
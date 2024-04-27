import sys
input = sys.stdin.readline 

T = int(input())
for _ in range(T):
    f_flag, s_flag = False, False
    n = int(input())
    first = list(map(int, input().split()))
    second = list(map(int, input().split()))
    
    dp = [0]*n
    dp[0] = max(first[0], second[0])
    selected = [[False]*2 for _ in range(n)]
    if n > 1:
        dp[1] = max(first[0]+second[1], second[0]+first[1])
        if first[0] + second[1] > second[0] + first[1]:
            selected[1][1] = True
        for i in range(2, n):
            dp[i] = max(max(first[i], second[i])+dp[i-2], dp[i-2]+first[i] if selected[i-1][0] else second[i])
    print(dp[-1])
            
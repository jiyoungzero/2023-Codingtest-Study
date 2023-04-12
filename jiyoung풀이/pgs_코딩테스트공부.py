# dp[i][j] = 알고력 i, 코딩력 j를 달성하는데에 필요한 최소 시간
# 단, 테이블의 크기 제한을 두는게 애매하기 때문에
# dp[alp_max][j] : 알고력 최대 "이상", 코딩력 j를 도달하는데에 필요한 최소시간

INF = int(1e9)

def solution(alp, cop, problems):
    dp = [[INF]*150 for _ in range(150)]
    alp_max = max(problem[0] for problem in problems)
    cop_max = max(problem[1] for problem in problems)
    alp = min(alp, alp_max)
    cop = min(cop, cop_max)
    
    dp[alp][cop] = 0
    
    for i in range(alp, alp_max+1):
        for j in range(cop, cop_max+1):
            dp[i+1][j] = min(dp[i+1][j], dp[i][j] + 1)
            dp[i][j+1] = min(dp[i][j+1], dp[i][j]+1)
            for alp_req, cop_req, alp_rwd, cop_rwd, cost in problems:
                if i < alp_req or j < cop_req:
                    continue
                else:
                    alp_nxt = min(alp_max, i+alp_rwd)
                    cop_nxt = min(cop_max, j+cop_rwd)
                    dp[alp_nxt][cop_nxt] = min(dp[alp_nxt][cop_nxt], cost+dp[i][j])
    return dp[alp_max][cop_max]
                 
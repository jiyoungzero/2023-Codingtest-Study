# 누적합

def solution(N, M, students, queries):
    answer = []
    income = [0]*300001 # 시작 지점 체크
    outcome = [0]*300001 # 끝 지점 체크
    dp = [0]*300001 # 누적합
    
    for [t, k] in students:
        income[t] += 1
        end = min(300000, t+k-1)
        outcome[end] += 1
    
    # 누적합 : gooooood...
    cur = 0
    for i in range(300001):
        cur += income[i]
        dp[i] = dp[i-1] + cur
        cur -= outcome[i]
    
    for (start, end) in queries:
        answer.append(dp[end]-dp[start-1])
    

    return answer

print(solution(5, 3, [[3, 2], [6, 3], [2, 8], [1, 5], [3, 4]], [[3, 7], [7, 9], [2, 5]])) 

# 정답 : [16, 5, 13] 

def solution(prices):
    answer = []
    n = len(prices)

    for i in range(n):
        now = prices[i]
        tmp = 0
        for j in range(i, n):
            if now <= prices[j]:tmp += 1
            else: 
                tmp += 1
                break
        answer.append(tmp-1)

    return answer
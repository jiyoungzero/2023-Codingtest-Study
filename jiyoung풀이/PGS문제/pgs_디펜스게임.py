def solution(n, k, enemy):
    answer = 0
    if len(enemy) <= k:return len(enemy)
    
    for e in enemy:
        if e > n and k == 0:
            break
        elif e <= n:
            answer += 1
            n -= e
        elif k > 0:
            k -= 1
            answer += 1
            continue

    return answer
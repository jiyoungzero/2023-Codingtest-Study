def solution(N, K):
    nums = [i for i in range(1, N+1)]
    answer = 0
    cur = 0

    while nums:
        nxt = (cur+K-1)%len(nums)
        cur = nxt
        answer= nums[cur]
        del nums[cur]

    return answer

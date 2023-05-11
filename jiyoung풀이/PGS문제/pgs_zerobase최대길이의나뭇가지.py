# 이진탐색 

def solution(N, branches):
    answer = -1
    branches.sort()
    left, right = 1, branches[-1] # 1,16 -> mid = 8

    while left < right:
        mid = left + (right-left) // 2
        tmp = 0
        print(left, right, mid)
        for b in branches:
            tmp += (b // mid)

        if N <= tmp and answer < mid:
            answer = mid
            left = mid + 1
        elif N <= tmp:
            # left = mid + 1
            break
        else:
            right = mid # left = 1, right = 8

    print(left, right)
    return answer

print(solution(20, [8, 15, 16, 18, 32, 16, 20, 15]))
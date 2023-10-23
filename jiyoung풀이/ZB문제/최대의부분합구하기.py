def solution(nums):
    N = len(nums)
    cum_nums = [0 for _ in range(N)]
    cum_nums[0] = nums[0]
    for i in range(1, N):
        cum_nums[i] = cum_nums[i-1] + nums[i]

    def S(l, r):
        if l == 0:
            return cum_nums[r]
        else:
            return cum_nums[r] - cum_nums[l-1]
        
    def solve(left, right):
        if left == right:
            return nums[left] * nums[left]
        
        mid = (left + right) // 2
        ret = max(solve(left, mid), solve(mid+1, right))
        
        l, r = mid, mid + 1
        mn = min(nums[l], nums[r])
        ret = max(ret, (nums[l] + nums[r]) * mn)
        
        while left < l or r < right:
            if (r < right) and (left == l or nums[l-1] < nums[r+1]):
                r += 1
                mn = min(mn, nums[r])
            else:
                l -= 1
                mn = min(mn, nums[l])
            ret = max(ret, S(l, r) * mn)
        return ret

    return solve(0, N-1)

# nums = [2, 5, 10, 9, 8, 5]
# print(solution(nums))
# 분할정복

# 문제
# 당신은 배열천재가 되기 위해 수련중이다. 배열천재가 되기 위해서는 조건에 맞는 부분 배열을 항상 빠르게 찾아낼 수 있어야 한다.

# 이번에 당신이 찾아야 하는 부분 배열의 조건은 아래와 같다.

# "부분 배열의 총 합과 부분 배열 중 가장 작은 원소의 곱을 부분 배열의 점수로 하자." (sum(subArray) * min(subArray))
# "이 때, 가장 높은 점수를 가지는 부분 배열을 찾아라."
# "단, 전체 배열의 모든 원소는 자연수이다."
# 예를 들면, 아래와 같은 배열이 주어졌다고 하자.

# nums = {2, 5, 10, 9, 8, 5}

# 이 때, 위 조건에 해당하는 부분 배열과 그 점수는 아래와 같다.

# {10, 9, 8} -> (10 + 9 + 8) * 8 = 216

# 위와 같이 주어진 배열 nums에서 조건에 맞는 부분 배열의 점수를 출력하시오.

# 입력설명
# 0 < nums.length <= 10000
# 0 < nums[i] <= 10000
# 출력설명
# 점수를 최대로 하는 부분 배열의 점수를 정수로 출력

# 모범답안

def solution(nums):
    n = len(nums)
    cum_nums = [0 for _ in range(n)]
    cum_nums[0] = nums[0]
    for i in range(1, n):
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
        
        l, r = mid, mid+1
        mn = min(nums[l], nums[r])
        ret = max(ret, (nums[l] + nums[r] * mn))
        
        while left < l or r<right:
            if ( r<right) and (left == 1 or nums[l-1] < nums[r+1]):
                r += 1
                mn = min(mn, nums[r])
                
            else:
                l -= 1
                mn = min(mn, nums[l])
            ret = max(ret, S(l,r)*mn)
        return ret
    return solve(0, n-1)
                
     
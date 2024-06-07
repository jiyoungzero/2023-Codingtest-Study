def dfs(nums, target, depth, cur):
    result = 0
    if depth == len(nums):
        if cur == target:
            return 1
        else: return 0
    result += dfs(nums, target, depth+1, cur+nums[depth])
    result += dfs(nums, target, depth+1, cur-nums[depth])
    
    return result 

def solution(numbers, target):
    answer = 0
    answer = dfs(numbers, target, 0, 0)
    
    return answer
# hash

# 레벨1
def solution(nums):
    answer = 0
    canTake = len(nums)//2
    kind = len(set(nums))
    
    if kind >= canTake:
        answer = canTake
    else:
        answer = kind
    return answer
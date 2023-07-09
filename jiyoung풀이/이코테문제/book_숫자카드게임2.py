def solution(n, m, arr):
    result = -1
    
    for i in range(len(arr)):
        target = min(arr[i])
        result = max(result, target)
    return result
    
print(solution(3,3,[[3,1,2],[4,1,4],[2,2,2]]))
print(solution(2,4,[[7,3,1,8],[3,3,3,4]]))
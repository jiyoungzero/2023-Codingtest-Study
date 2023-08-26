# 16점. 오답
def solution(arr):
    answer = 'YES'
    for i in range(1, len(arr)//2):
        p, l, r = arr[i], arr[i*2], arr[i*2+1]

        if min([p,l,r]) == p and l <= r:
            continue
        else:
            return "NO"
    return answer
print(solution([0,2,2,2]))
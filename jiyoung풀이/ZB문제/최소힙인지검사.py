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

# 정답! 
def solution(arr):
    answer = 'YES'
    for i in range(1, len(arr)):
        p, c = arr[(i-1)//2], arr[i]
        if p <= c:
            continue
        else:
            return "NO"
    return answer
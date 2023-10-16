# 230426

def solution(A):
    # Implement your solution here
    answer = 0
    target = set(A)
    A.sort(reverse=True)
    sorted(list(target)).reverse(True)
    for num in target:
        if num == A.count(num):
            answer = max(answer, num)
    return answer
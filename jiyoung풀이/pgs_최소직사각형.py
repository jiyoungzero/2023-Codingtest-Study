# 완전탐색

# 내풀이 -> 시간 오래 걸림
def solution(sizes):
    answer = 0
    width = []
    height = []

    for ele in sizes:
        if ele[0] > ele[1]:
            width.append(ele[0])
            height.append(ele[1])
        else:
            width.append(ele[1])
            height.append(ele[0])


    return max(width)*max(height)
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


# 더 큰 수로 swap -> 매번 돌릴 때 마다 최댓값으로 들어가도록 하기
def solution(sizes):
    width = 0
    height = 0
    
    for a,b in sizes:
        if a<b:a,b =b, a
        width = max(width, a)
        height = max(height, b)
            
    
    return width*height
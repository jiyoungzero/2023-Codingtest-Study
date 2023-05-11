# 이진탐색 

# 2대의 치킨 튀김기,
# fry 각 튀김기가 튀겨지는데 걸리는 시간 / clean fry후 다음 작업을 위해 필요한 시간 
# fry[i] + clean[i] == 1대의 치킨 튀김기가 걸리는 시간 
# (3)5,(6)7-> 58이면 12번, 8번 튀김 ) // M = 목표 치킨 수 
def solution(N, M, fry, clean):
    answer = 0
    left , right = 1, 0
    for f, c in zip(fry, clean):
        if right < (f+c)*M:
            right = (f+c)*M
        else:continue

    while left < right:
        mid = left + right // 2
        tmp = 0
        for f, c in zip(fry, clean):
            tmp += (f+c)//mid
            tmp += ((f+c)%mid)//f
        if tmp >= M and tmp > answer:
            answer = mid
        else:
            right = mid 

    print(left, right)
    return answer
# 문제 : 

# 내 풀이 : 30분 초과함
def solution(brown, yellow):
    S = brown + yellow
    arr = []
    ans = []
    for i in range(2, S):
        if S % i == 0:
            arr.append([i, S//i])

    for i in range(len(arr)):
        l,r = arr[i][0]-2, arr[i][1]-2
        if yellow == (l*r):
            if arr[i][0] >= arr[i][1]:
                ans = [arr[i][0], arr[i][1]]
    return ans

# 이거 풀이 다시 보기
# 다른 사람 풀이
def solution(brown, red):
    for i in range(1, int(red**(1/2))+1): # yellow의 sqrt 값까지 탐색(시간단축!)
        if red % i == 0: # 제곱근이라면
            if 2*(i + red//i) == brown-4:
                return [red//i+2, i+2]
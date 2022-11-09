# 문제 스스로 풀어보기 

# dp...
# 감이 안와요...


# 정답 풀이 :
# 1. 인덱스 자체 생성
# 2. visited 배열을 dp배열의 인접행렬의 성분의 합으로 나타내기
# 즉 1분 전의 정보를 (인접행렬) 넘겨준다 
# 3. dp배열을 10번 반복


# 1: 전산관
# 2: 미래관
# 3: 신앙관
# 4: 한경직
# 5: 진리관
# 6: 학생회관
# 7: 형남공
import sys
input = sys.stdin.readline

d = int(input())
dp = [1,0,0,0,0,0,0,0]

def nxt(lst):
    tmp = [0 for _ in range(8)]
    tmp[0] = lst[1] + lst[2]
    tmp[1] = lst[0] + lst[2] + lst[3]
    tmp[2] = lst[0] + lst[1]+ lst[3] + lst[4]
    tmp[3] = lst[1] + lst[2] + lst[4] + lst[5]
    tmp[4] = lst[2] + lst[3] + lst[5] + lst[7]
    tmp[5] = lst[3] + lst[4] + lst[6]
    tmp[6] = lst[5] + lst[7]
    tmp[7] = lst[4] + lst[6]
    return tmp

for _ in range(d):
    dp = nxt(dp)
print(dp[0] % 1000000007)


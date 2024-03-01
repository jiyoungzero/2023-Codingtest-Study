import sys
input = sys.stdin.readline 

# [좋아하는 학생 수, 빈 자리 수, 행번호, 열번호]
# sort(key = lambda x : (-x[0], -x[1], x[2], x[3]))



def is_adj(r1, c1, r2, c2):
    return abs(r1-r2)+abs(c1-c2) == 1


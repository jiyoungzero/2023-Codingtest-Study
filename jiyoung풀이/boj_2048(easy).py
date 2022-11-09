# 문제 스스로 풀어보기 
# 삼성 코테 성격을 띄는 문제 --> 중요!

# 감이 안잡혀서 정답 코드를 보고 공부햇음 

from copy import deepcopy # 이거 외우기!
import sys
input = sys.stdin.readline

N = int(input())
B = [list(map(int, input().split())) for _ in range(N)]

# 왼쪽 회전 
def rotate(A, N):
    X = deepcopy(A)
    for i in range(N):
        for j in range(N): 
            X[N-j-1][i] = A[i][j]
    return X

def convert(l):
    ll = [i for i in l if i]
    for i in range(len(ll)-1):
        if ll[i] == ll[i+1]:
            ll[i] *= 2
            ll[i+1] = 0
    ll = [i for i in ll if i]
    return ll + [0]*(len(l)-len(ll)) # 원래 l 만큼의 리스트 개수로 만듦

def dfs(A, s, N):
    ret = max([max[i] for i in A])
    if s == 0:return ret
    
    for _ in range(4):
        X = [convert(i) for i in A]
        if A != X : 
            ret=max(ret, dfs(X, s-1, N))
        A = rotate(A, N)
    return ret

print(dfs(B, 5, N))


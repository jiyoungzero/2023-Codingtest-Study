# 분할정복

def solution(n, i, j):
    answer = 0
    return recursion(0,n,i,j)

def recursion(count, n, i, j):
    if n == 2:
        if i==0 and j== 1:
            return count + 1
        elif i==0 and j==0:
            return count + 2
        elif i==1 and j == 0:
            return count + 3
        else:
            return count + 4
    # 4개영역으로 나누어 offset 계산 
    m = n//2
    # 1
    if 0<=i<m and m<=j:
        return recursion(count, m, i, j-m)
    # 2
    if 0<=i<m and 0<=j<m:
        count += (m**2*1)
        return recursion(count, m, i, j)
    # 3
    if m<=i and 0<=j<m:
        count += (m**2*2)
        return recursion(count , m, i-m, j)
    # 4
    if m<=i and m<=j:
        count += (m**2*3)
        return recursion(count, m, i-m, j-m)
# 20 * 20이므로 1억 이하의 연산이 최대로 걸린다. -> 완전 탐색으로 해결할 수 있다. (구현)
# <전략>
# 자물쇠의 크기를 3배 이상으로 변경하면 좋음
# 자물쇠 + 열쇠 값을 더했을 때 모두 1이면 된다. 
# rotate_90degree() 함수는 외우기

def rotate_90degree(arr):
    n, m = len(arr), len(arr[0])
    result = [[0]*n for _ in range(m)] # 회전결과 값이니까
    
    for i in range(n):
        for j in range(m):
            result[j][n-i-1] = arr[i][j]
    return result
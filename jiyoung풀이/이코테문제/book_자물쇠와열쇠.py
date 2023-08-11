# 20 * 20이므로 1억 이하의 연산이 최대로 걸린다. -> 완전 탐색으로 해결할 수 있다. (구현)
# <전략>
# 자물쇠의 크기를 3배 이상으로 변경하면 좋음
# 자물쇠 + 열쇠 값을 더했을 때 모두 1이면 된다. 
# rotate_90degree() 함수는 외우기


def rotate_90degree(arr):
    n, m = len(arr), len(arr[0])
    result = [[0]*n for _ in range(m)]

    for i in range(n):
        for j in range(m):
            result[j][n-i-1] = arr[i][j]
    return result

def check(l_arr):
    len_arr = len(l_arr)//3

    for i in range(len_arr, len_arr*2):
        for j in range(len_arr, len_arr*2):
            if l_arr[i][j] != 1:
                return False

    return True


def solution(key, lock):
    answer = False
    len_key, len_lock = len(key), len(lock)

    # 3배로 늘리기
    new_lock = [[0]*len_lock*3 for _ in range(len_lock*3)]

    for i in range(len_lock):
        for j in range(len_lock):
            new_lock[i+len_lock][j+len_lock] = lock[i][j]

    # 4가지 방향에 대해서 검사
    for rotation in range(4):
        key = rotate_90degree(key)
        # 열쇠 끼워넣기
        for x in range(len_lock*2):
            for y in range(len_lock*2):
                for i in range(len_key):
                    for j in range(len_key):
                        new_lock[x+i][y+j] += key[i][j]
                # 열쇠가 맞는지 검사
                if check(new_lock):
                    return True
                # 안맞으면 열쇠 빼기
                for i in range(len_key):
                    for j in range(len_key):
                        new_lock[x+i][y+j] -= key[i][j]

    return answer
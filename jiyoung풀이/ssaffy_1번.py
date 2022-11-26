import sys
input = sys.stdin.readline

T = int(input())

for t in range(T):
    result = 0
    M, N = map(int, input().split())
    arr = [[0]*M for _ in range(M)]

    low_idx = []
    r_l_idx = []
    for _ in range(N):
        a, b = map(int, input().split())
        low_idx.append(a)
        r_l_idx.append(b)

    # 위로 올리기
    low_max_idx = max(low_idx)
    if low_max_idx == 0:
        result = 0
    else:
        for _ in range(low_max_idx):result+=1

    # 양옆 이동
    r_l_max_idx = (M-1) - max(sorted(r_l_idx)[0], M-sorted(r_l_idx)[-1])
    for _ in range(r_l_max_idx): result += 1

    print(f"#{t+1} {result}")
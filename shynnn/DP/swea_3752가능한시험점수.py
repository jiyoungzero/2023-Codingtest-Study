# 복습
# 46분 시작
# DP

T = int(input())
for t in range(1, T+1):
    N = int(input())
    arr = list(map(int, input().split()))
    visited = [0 for _ in range(N)]
    result = set()
    result.add(0)

    # 2 3 5

    for a in arr:  # 중복 제거
        for r in list(result):
            result.add(r + a)

    result = set(result)
    print(f"#{t} {len(result)}")

# 문제 스스로 풀어보기 35분시작


T = int(input())

for t in range(1, T+1):
    result = 0
    n = int(input())
    arr = [list(map(int, input())) for _ in range(n)]

    s, e = n//2, n//2
    for i in range(n):
        for j in range(s, e+1):
            print(i, j)
            result += arr[i][j]
        
        if i < n//2:
            s -= 1
            e += 1
        else:
            s += 1
            e -= 1
    
    print(f"#{t} {result}")
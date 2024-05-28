import sys
input = sys.stdin.readline 


n, k = map(int, input().split())
arr = list(map(int, input().split()))
answer = int(1e9)

# 1이 k개 이상 포함된, 연속된 가장 작은 길이
s, e = 0, 0
cnt = 1 if arr[s] == 1 else 0
# 왼쪽 포인터, 오른쪽 포인터 둘 중 하나가 끝에 도달할 때까지 반복한다.
while e < n:
    # 라이언 인형의 개수가 부족하다면, 오른쪽 포인터를 옮겨 본다.
    if cnt < k:
        e += 1
        if e < n and arr[e] == 1:
            cnt += 1
    # 라이언 인형의 개수가 충분하다면, 왼쪽 포인터를 옮겨 본다.
    else:
        answer = min(answer, (e-s+1))
        s += 1
        if arr[s-1] == 1:
            cnt -= 1

print(answer)
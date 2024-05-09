import sys
input = sys.stdin.readline 


# 완탐으로 풀 수 있으나, 이분탐색으로 하면 더 빠르다! 기억하자
n, k = map(int, input().split())
answer = False

# 가로로 자르는 횟수 row
# 세로로 자르는 횟수 col
# 나오는 총 색종이 조각 : (row + 1) * (col + 1) 
# l, r = 0, n
# while l <= r:
#     row = (l+r)//2
#     col = n - row
    
#     cnt = (row+1)*(col+1)
#     if cnt == k:
#         answer = True
#         break
#     elif cnt > k:
#         r = row - 1
#     else:
#         l = row + 1
l, r = 0, n
while l <= r:
    mid = (l+r) // 2
    
    cnt = (mid+1)*(n-mid+1)
    if cnt == k:
        answer = True
        break
    elif cnt > k:
        r = mid - 1
    else:
        l = mid + 1

if answer:
    print("YES")
else:
    print("NO")
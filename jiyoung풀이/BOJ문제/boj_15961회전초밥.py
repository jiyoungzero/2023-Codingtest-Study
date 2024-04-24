import sys
input = sys.stdin.readline 

n, d, k, c = map(int, input().split())
arr = [int(input()) for _ in range(n)]
answer = 0
# k개를 연속으로 선택했을 때 가장 set의 개수가 많은 것 (기본 set = (c))


s, e = 0, k
while s != n:
    tmp = set()
    if s > e:
        tmp = set([c]) | set(arr[s:n]) | set(arr[:e])
    else:
        tmp = set([c]) | set(arr[s:e])
    print(tmp, s, e)
    if len(tmp) > answer:
        answer = len(tmp)
    s += 1
    e = (s+k)%n
print(answer)    
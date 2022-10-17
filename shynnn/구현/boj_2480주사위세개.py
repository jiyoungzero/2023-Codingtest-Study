# 브론즈 4
# 3 :10,000원+(같은 눈)×1,000원
# 2 : 1,000원+(같은 눈)×100원
# 모두 다름 : (그 중 가장 큰 눈)×100원

# set을 사용해서 길이로 ? -> 어떤 것이 같은 눈인지 알수 없음

import sys
input = sys.stdin.readline

a, b, c = map(int, input().split())

if a == b == c:
    print(10000 + 1000*a)
    exit(0)
elif a == b:
    print(1000 + 100*a)
    exit(0)
elif b == c:
    print(1000 + 100 * b)
    exit(0)
elif a == c:
    print(1000 + 100 * a)
    exit(0)

elif a != b and b != c and a != c:
    m = max(a, b, c)
    print(m*100)
    exit(0)

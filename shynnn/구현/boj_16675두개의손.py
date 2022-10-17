# 브론즈 2
# 제한시간 0.1초
import sys
input = sys.stdin.readline

Ml, Mr, Tl, Tr = map(str, input().strip().split(' '))


# S R P, 가위 바위 보
# S < R, R < P, P < S
# 양손 경우의 수 6가지 (순서는 상관 X)

# 민성 무조건 이김 MS, 태경 무조건 이김 TK, 확답 X ?

# 둘다 다를 경우
if Ml != Mr and Tl != Tr:
    print("?")

# MS만 같을 경우
elif Ml == Mr and Tl != Tr:
    if Ml == 'S' and (Tl == 'R' or Tr == 'R'):
        print("TK")
    elif Ml == 'P' and (Tl == 'S' or Tr == 'S'):
        print("TK")
    elif Ml == 'R' and (Tl == 'P' or Tr == 'P'):
        print("TK")
    else:
        print("?")

# TK만 같을 경우
elif Ml != Mr and Tl == Tr:
    if Tl == 'S' and (Ml == 'R' or Mr == 'R'):
        print("MS")
    elif Tl == 'P' and (Ml == 'S' or Mr == 'S'):
        print("MS")
    elif Tl == 'R' and (Ml == 'P' or Mr == 'P'):
        print("MS")
    else:
        print("?")

# 둘다 같을 경우
else:
    if Ml == 'S':
        if Tl == 'P':
            print("MS")
        if Tl == 'S':
            print("?")
        if Tl == 'R':
            print("TK")
    if Ml == 'R':
        if Tl == 'P':
            print("TK")
        if Tl == 'S':
            print("MS")
        if Tl == 'R':
            print("?")
    if Ml == 'P':
        if Tl == 'P':
            print("?")
        if Tl == 'S':
            print("TK")
        if Tl == 'R':
            print("MS")

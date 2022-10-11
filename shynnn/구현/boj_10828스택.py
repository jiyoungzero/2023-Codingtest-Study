# 자료구조, 스택, 시뮬레이션
# 실버 4, 하, 20분
# 10분만에 풀이 , 시간초과.. 왜..? ->sys로 해결

# 명령의 수

import sys
input = sys.stdin.readline  # 빠른 입력함수

n = int(input())
arr = []
for _ in range(n):
    cmd = input().strip().split(' ')  # 공백 제거 .strip() 해야함
    # list(map(str, input().split(' ')))

    if cmd[0] == 'push':
        arr.append(int(cmd[1]))
    elif cmd[0] == 'size':
        print(len(arr))
    elif cmd[0] == 'empty':
        if arr:
            print('0')
        else:
            print('1')
    elif cmd[0] == 'pop':
        if not arr:
            print('-1')
        else:
            print(arr.pop())
    elif cmd[0] == 'top':
        if not arr:
            print('-1')
        else:
            print(arr[-1])

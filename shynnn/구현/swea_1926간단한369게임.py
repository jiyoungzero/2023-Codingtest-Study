# D2

N = int(input())
clap = ['3', '6', '9']

for num in range(1, N+1):
    cnt = 0
    for i in str(num):
        if i in clap:
            cnt += 1
    if cnt != 0:
        print("-" * cnt, end=' ')
    else:
        print(num, end=' ')

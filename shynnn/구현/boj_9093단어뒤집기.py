# 브론즈 1

test_case = int(input())
result = []
for _ in range(test_case):
    sentence = list(input().strip().split())

    # 2차원 배열
    for i in range(len(sentence)):
        sentence[i] = list(sentence[i][::-1])

    for i in range(len(sentence)):
        print(''.join(sentence[i]), end=" ")
    print("")

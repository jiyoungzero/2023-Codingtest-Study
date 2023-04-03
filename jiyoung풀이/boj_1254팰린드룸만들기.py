import sys
input =sys.stdin.readline

input = input().rstrip()
answer = 0

if input == input[::-1]:
    answer = len(input)
    print(answer)
else:
    for i in range(len(input)):
        for j in range(i+1, len(input)):
            tmp = list(input)
            plus = reversed(input[i:j])
            tmp += plus
            reversed_input = list(reversed(tmp))
            if tmp == reversed_input:
                answer = len(input) + (j-i)
                print(answer)
                exit(0)

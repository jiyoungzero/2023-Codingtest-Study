import sys
input =sys.stdin.readline

input = input().rstrip()
answer = 0

if input == input[::-1]:
    answer = len(input)
else:
    reversed_input = list(reversed(input))
    start = 0
    for i in range(len(input)):
        if reversed_input[0] == input[i]:
            start = i
            break
    answer = len(input) + start
print(answer)

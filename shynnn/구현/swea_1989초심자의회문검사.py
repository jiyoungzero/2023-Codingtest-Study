# D2
# 8분 시작

from copy import deepcopy


T = int(input())
for t in range(1, T + 1):
    sentence = list(input().strip())
    result = 0
    origin_sentence = deepcopy(sentence)  # =으로 하면 주소로 참조하는 걸로 됨
    sentence.reverse()
    if (sentence == origin_sentence):
        result = 1
    print("#{} {}".format(t, result))

# 다른 풀이 1- 하나하나 비교
# for t in range(1, T+1) :
#     word = input()
#     for i in range(len(word)//2) :
#         if word[i] == word[-1-i] :
#             answer = 1
#         else :
#             answer = 0
#     print("#{} {}".format(t, answer))

# 다른 풀이 2 - slicing 사용
# test_case = int(input())

# for i in range(test_case):
#     word = input()
#     result = 0
#     if word == word[::-1]:
#         result = 1

#     else:
#         result = 0
#     print("#{} {}".format(t, result))

# 정렬

# 다시 보기
def solution(numbers):
    answer = ''
    new_numbers = list(map(str, numbers))
    new_numbers.sort(reverse=True, key = lambda x:x*3)

    # print("".join(new_numbers))


    return str(int("".join(new_numbers)))
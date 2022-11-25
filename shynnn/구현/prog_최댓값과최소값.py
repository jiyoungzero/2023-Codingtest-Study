def solution(s):
    arr = list(map(int, s.split(' ')))
    return str(min(arr)) + " " + str(max(arr))

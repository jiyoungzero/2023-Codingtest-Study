# 카카오 기출 문제
# 문자열
# N 이 10만 일때는 NlogN으로 풀어야함.
#!/bin/python3


# Complete the 'camelcase' function below.
# The function is expected to return an INTEGER.
# The function accepts STRING s as parameter.


def camelcase(s):
    # Write your code here
    string = list(s.rstrip())
    string.sort()
    count = 0
    for s in string:
        if ord(s) > 90:
            break
        count += 1
    return count+1


if __name__ == '__main__':

    s = input()
    result = camelcase(s)
    print(result)

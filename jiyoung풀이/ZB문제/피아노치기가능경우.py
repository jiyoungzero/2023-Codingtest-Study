def solution(s):
    start = 0
    cnt = 0
    while start < len(s):
        if s[start] == "1":
            start += 3
            cnt += 1
        else:
            start += 1
    return "YES" if cnt%2 == 0 else "NO"